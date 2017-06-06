""" ietf_netconf_monitoring 

NETCONF Monitoring Module.
All elements in this module are read\-only.

Copyright (c) 2010 IETF Trust and the persons identified as
authors of the code. All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD
License set forth in Section 4.c of the IETF Trust's
Legal Provisions Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6022; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class NetconfDatastoreTypeEnum(Enum):
    """
    NetconfDatastoreTypeEnum

    Enumeration of possible NETCONF datastore types.

    .. data:: running = 0

    .. data:: candidate = 1

    .. data:: startup = 2

    """

    running = 0

    candidate = 1

    startup = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['NetconfDatastoreTypeEnum']



class TransportIdentity(object):
    """
    Base identity for NETCONF transport types.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['TransportIdentity']['meta_info']


class SchemaFormatIdentity(object):
    """
    Base identity for data model schema languages.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['SchemaFormatIdentity']['meta_info']


class NetconfState(object):
    """
    The netconf\-state container is the root of the monitoring
    data model.
    
    .. attribute:: capabilities
    
    	Contains the list of NETCONF capabilities supported by the server
    	**type**\:   :py:class:`Capabilities <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Capabilities>`
    
    .. attribute:: datastores
    
    	Contains the list of NETCONF configuration datastores
    	**type**\:   :py:class:`Datastores <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores>`
    
    .. attribute:: schemas
    
    	Contains the list of data model schemas supported by the server
    	**type**\:   :py:class:`Schemas <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Schemas>`
    
    .. attribute:: sessions
    
    	The sessions container includes session\-specific data for NETCONF management sessions.  The session list MUST include all currently active NETCONF sessions
    	**type**\:   :py:class:`Sessions <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Sessions>`
    
    .. attribute:: statistics
    
    	Statistical data pertaining to the NETCONF server
    	**type**\:   :py:class:`Statistics <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Statistics>`
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        self.capabilities = NetconfState.Capabilities()
        self.capabilities.parent = self
        self.datastores = NetconfState.Datastores()
        self.datastores.parent = self
        self.schemas = NetconfState.Schemas()
        self.schemas.parent = self
        self.sessions = NetconfState.Sessions()
        self.sessions.parent = self
        self.statistics = NetconfState.Statistics()
        self.statistics.parent = self


    class Capabilities(object):
        """
        Contains the list of NETCONF capabilities supported by the
        server.
        
        .. attribute:: capability
        
        	List of NETCONF capabilities supported by the server
        	**type**\:  list of str
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            self.parent = None
            self.capability = YLeafList()
            self.capability.parent = self
            self.capability.name = 'capability'

        @property
        def _common_path(self):

            return '/ietf-netconf-monitoring:netconf-state/ietf-netconf-monitoring:capabilities'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.capability is not None:
                for child in self.capability:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
            return meta._meta_table['NetconfState.Capabilities']['meta_info']


    class Datastores(object):
        """
        Contains the list of NETCONF configuration datastores.
        
        .. attribute:: datastore
        
        	List of NETCONF configuration datastores supported by the NETCONF server and related information
        	**type**\: list of    :py:class:`Datastore <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore>`
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            self.parent = None
            self.datastore = YList()
            self.datastore.parent = self
            self.datastore.name = 'datastore'


        class Datastore(object):
            """
            List of NETCONF configuration datastores supported by
            the NETCONF server and related information.
            
            .. attribute:: name  <key>
            
            	Name of the datastore associated with this list entry
            	**type**\:   :py:class:`NetconfDatastoreTypeEnum <ydk.models.ietf.ietf_netconf_monitoring.NetconfDatastoreTypeEnum>`
            
            .. attribute:: locks
            
            	The NETCONF <lock> and <partial\-lock> operations allow a client to lock specific resources in a datastore.  The NETCONF server will prevent changes to the locked resources by all sessions except the one that acquired the lock(s).  Monitoring information is provided for each datastore entry including details such as the session that acquired the lock, the type of lock (global or partial) and the list of locked resources.  Multiple locks per datastore are supported
            	**type**\:   :py:class:`Locks <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ncm'
            _revision = '2010-10-04'

            def __init__(self):
                self.parent = None
                self.name = None
                self.locks = None


            class Locks(object):
                """
                The NETCONF <lock> and <partial\-lock> operations allow
                a client to lock specific resources in a datastore.  The
                NETCONF server will prevent changes to the locked
                resources by all sessions except the one that acquired
                the lock(s).
                
                Monitoring information is provided for each datastore
                entry including details such as the session that acquired
                the lock, the type of lock (global or partial) and the
                list of locked resources.  Multiple locks per datastore
                are supported.
                
                .. attribute:: global_lock
                
                	Present if the global lock is set
                	**type**\:   :py:class:`GlobalLock <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks.GlobalLock>`
                
                .. attribute:: partial_lock
                
                	List of partial locks
                	**type**\: list of    :py:class:`PartialLock <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks.PartialLock>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ncm'
                _revision = '2010-10-04'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.global_lock = NetconfState.Datastores.Datastore.Locks.GlobalLock()
                    self.global_lock.parent = self
                    self.partial_lock = YList()
                    self.partial_lock.parent = self
                    self.partial_lock.name = 'partial_lock'


                class GlobalLock(object):
                    """
                    Present if the global lock is set.
                    
                    .. attribute:: locked_by_session
                    
                    	The session ID of the session that has locked this resource.  Both a global lock and a partial lock MUST contain the NETCONF session\-id.  If the lock is held by a session that is not managed by the NETCONF server (e.g., a CLI session), a session id of 0 (zero) is reported
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: locked_time
                    
                    	The date and time of when the resource was locked
                    	**type**\:  str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ncm'
                    _revision = '2010-10-04'

                    def __init__(self):
                        self.parent = None
                        self.locked_by_session = None
                        self.locked_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-netconf-monitoring:global-lock'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.locked_by_session is not None:
                            return True

                        if self.locked_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
                        return meta._meta_table['NetconfState.Datastores.Datastore.Locks.GlobalLock']['meta_info']


                class PartialLock(object):
                    """
                    List of partial locks.
                    
                    .. attribute:: lock_id  <key>
                    
                    	This is the lock id returned in the <partial\-lock> response
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: locked_by_session
                    
                    	The session ID of the session that has locked this resource.  Both a global lock and a partial lock MUST contain the NETCONF session\-id.  If the lock is held by a session that is not managed by the NETCONF server (e.g., a CLI session), a session id of 0 (zero) is reported
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: locked_node
                    
                    	The list of instance\-identifiers (i.e., the locked nodes).  The scope of the partial lock is defined by the list of locked nodes
                    	**type**\:  list of str
                    
                    .. attribute:: locked_time
                    
                    	The date and time of when the resource was locked
                    	**type**\:  str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    	**mandatory**\: True
                    
                    .. attribute:: select
                    
                    	The xpath expression that was used to request the lock.  The select expression indicates the original intended scope of the lock
                    	**type**\:  list of str
                    
                    

                    """

                    _prefix = 'ncm'
                    _revision = '2010-10-04'

                    def __init__(self):
                        self.parent = None
                        self.lock_id = None
                        self.locked_by_session = None
                        self.locked_node = YLeafList()
                        self.locked_node.parent = self
                        self.locked_node.name = 'locked_node'
                        self.locked_time = None
                        self.select = YLeafList()
                        self.select.parent = self
                        self.select.name = 'select'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.lock_id is None:
                            raise YPYModelError('Key property lock_id is None')

                        return self.parent._common_path +'/ietf-netconf-monitoring:partial-lock[ietf-netconf-monitoring:lock-id = ' + str(self.lock_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.lock_id is not None:
                            return True

                        if self.locked_by_session is not None:
                            return True

                        if self.locked_node is not None:
                            for child in self.locked_node:
                                if child is not None:
                                    return True

                        if self.locked_time is not None:
                            return True

                        if self.select is not None:
                            for child in self.select:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
                        return meta._meta_table['NetconfState.Datastores.Datastore.Locks.PartialLock']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-netconf-monitoring:locks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.global_lock is not None and self.global_lock._has_data():
                        return True

                    if self.partial_lock is not None:
                        for child_ref in self.partial_lock:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
                    return meta._meta_table['NetconfState.Datastores.Datastore.Locks']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-netconf-monitoring:netconf-state/ietf-netconf-monitoring:datastores/ietf-netconf-monitoring:datastore[ietf-netconf-monitoring:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.locks is not None and self.locks._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
                return meta._meta_table['NetconfState.Datastores.Datastore']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf-monitoring:netconf-state/ietf-netconf-monitoring:datastores'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.datastore is not None:
                for child_ref in self.datastore:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
            return meta._meta_table['NetconfState.Datastores']['meta_info']


    class Schemas(object):
        """
        Contains the list of data model schemas supported by the
        server.
        
        .. attribute:: schema
        
        	List of data model schemas supported by the server
        	**type**\: list of    :py:class:`Schema <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Schemas.Schema>`
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            self.parent = None
            self.schema = YList()
            self.schema.parent = self
            self.schema.name = 'schema'


        class Schema(object):
            """
            List of data model schemas supported by the server.
            
            .. attribute:: identifier  <key>
            
            	Identifier to uniquely reference the schema.  The identifier is used in the <get\-schema> operation and may be used for other purposes such as file retrieval.  For modeling languages that support or require a data model name (e.g., YANG module name) the identifier MUST match that name.  For YANG data models, the identifier is the name of the module or submodule.  In other cases, an identifier such as a filename MAY be used instead
            	**type**\:  str
            
            .. attribute:: version  <key>
            
            	Version of the schema supported.  Multiple versions MAY be supported simultaneously by a NETCONF server.  Each version MUST be reported individually in the schema list, i.e., with same identifier, possibly different location, but different version.  For YANG data models, version is the value of the most recent YANG 'revision' statement in the module or submodule, or the empty string if no 'revision' statement is present
            	**type**\:  str
            
            .. attribute:: format  <key>
            
            	The data modeling language the schema is written in (currently xsd, yang, yin, rng, or rnc). For YANG data models, 'yang' format MUST be supported and 'yin' format MAY also be provided
            	**type**\:   :py:class:`SchemaFormatIdentity <ydk.models.ietf.ietf_netconf_monitoring.SchemaFormatIdentity>`
            
            .. attribute:: location
            
            	One or more locations from which the schema can be retrieved.  This list SHOULD contain at least one entry per schema.  A schema entry may be located on a remote file system (e.g., reference to file system for ftp retrieval) or retrieved directly from a server supporting the <get\-schema> operation (denoted by the value 'NETCONF')
            	**type**\: one of the below types:
            
            	**type**\:  list of   :py:class:`LocationEnum <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Schemas.Schema.LocationEnum>`
            
            
            ----
            	**type**\:  list of str
            
            
            ----
            .. attribute:: namespace
            
            	The XML namespace defined by the data model.  For YANG data models, this is the module's namespace. If the list entry describes a submodule, this field contains the namespace of the module to which the submodule belongs
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ncm'
            _revision = '2010-10-04'

            def __init__(self):
                self.parent = None
                self.identifier = None
                self.version = None
                self.format = None
                self.location = YLeafList()
                self.location.parent = self
                self.location.name = 'location'
                self.namespace = None

            class LocationEnum(Enum):
                """
                LocationEnum

                One or more locations from which the schema can be

                retrieved.  This list SHOULD contain at least one

                entry per schema.

                A schema entry may be located on a remote file system

                (e.g., reference to file system for ftp retrieval) or

                retrieved directly from a server supporting the

                <get\-schema> operation (denoted by the value 'NETCONF').

                .. data:: NETCONF = 0

                """

                NETCONF = 0


                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
                    return meta._meta_table['NetconfState.Schemas.Schema.LocationEnum']


            @property
            def _common_path(self):
                if self.identifier is None:
                    raise YPYModelError('Key property identifier is None')
                if self.version is None:
                    raise YPYModelError('Key property version is None')
                if self.format is None:
                    raise YPYModelError('Key property format is None')

                return '/ietf-netconf-monitoring:netconf-state/ietf-netconf-monitoring:schemas/ietf-netconf-monitoring:schema[ietf-netconf-monitoring:identifier = ' + str(self.identifier) + '][ietf-netconf-monitoring:version = ' + str(self.version) + '][ietf-netconf-monitoring:format = ' + str(self.format) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.identifier is not None:
                    return True

                if self.version is not None:
                    return True

                if self.format is not None:
                    return True

                if self.location is not None:
                    for child in self.location:
                        if child is not None:
                            return True

                if self.namespace is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
                return meta._meta_table['NetconfState.Schemas.Schema']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf-monitoring:netconf-state/ietf-netconf-monitoring:schemas'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.schema is not None:
                for child_ref in self.schema:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
            return meta._meta_table['NetconfState.Schemas']['meta_info']


    class Sessions(object):
        """
        The sessions container includes session\-specific data for
        NETCONF management sessions.  The session list MUST include
        all currently active NETCONF sessions.
        
        .. attribute:: session
        
        	All NETCONF sessions managed by the NETCONF server MUST be reported in this list
        	**type**\: list of    :py:class:`Session <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Sessions.Session>`
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            self.parent = None
            self.session = YList()
            self.session.parent = self
            self.session.name = 'session'


        class Session(object):
            """
            All NETCONF sessions managed by the NETCONF server
            MUST be reported in this list.
            
            .. attribute:: session_id  <key>
            
            	Unique identifier for the session.  This value is the NETCONF session identifier, as defined in RFC 4741
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: in_bad_rpcs
            
            	Number of messages received when an <rpc> message was expected, that were not correct <rpc> messages.  This includes XML parse errors and errors on the rpc layer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_rpcs
            
            	Number of correct <rpc> messages received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: login_time
            
            	Time at the server at which the session was established
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**mandatory**\: True
            
            .. attribute:: out_notifications
            
            	Number of <notification> messages sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_rpc_errors
            
            	Number of <rpc\-reply> messages sent that contained an <rpc\-error> element
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: source_host
            
            	Host identifier of the NETCONF client.  The value returned is implementation specific (e.g., hostname, IPv4 address, IPv6 address)
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            
            ----
            	**type**\:  str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
            
            
            ----
            .. attribute:: transport
            
            	Identifies the transport for each session, e.g., 'netconf\-ssh', 'netconf\-soap', etc
            	**type**\:   :py:class:`TransportIdentity <ydk.models.ietf.ietf_netconf_monitoring.TransportIdentity>`
            
            	**mandatory**\: True
            
            .. attribute:: username
            
            	The username is the client identity that was authenticated by the NETCONF transport protocol.  The algorithm used to derive the username is NETCONF transport protocol specific and in addition specific to the authentication mechanism used by the NETCONF transport protocol
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ncm'
            _revision = '2010-10-04'

            def __init__(self):
                self.parent = None
                self.session_id = None
                self.in_bad_rpcs = None
                self.in_rpcs = None
                self.login_time = None
                self.out_notifications = None
                self.out_rpc_errors = None
                self.source_host = None
                self.transport = None
                self.username = None

            @property
            def _common_path(self):
                if self.session_id is None:
                    raise YPYModelError('Key property session_id is None')

                return '/ietf-netconf-monitoring:netconf-state/ietf-netconf-monitoring:sessions/ietf-netconf-monitoring:session[ietf-netconf-monitoring:session-id = ' + str(self.session_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.session_id is not None:
                    return True

                if self.in_bad_rpcs is not None:
                    return True

                if self.in_rpcs is not None:
                    return True

                if self.login_time is not None:
                    return True

                if self.out_notifications is not None:
                    return True

                if self.out_rpc_errors is not None:
                    return True

                if self.source_host is not None:
                    return True

                if self.transport is not None:
                    return True

                if self.username is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
                return meta._meta_table['NetconfState.Sessions.Session']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf-monitoring:netconf-state/ietf-netconf-monitoring:sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.session is not None:
                for child_ref in self.session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
            return meta._meta_table['NetconfState.Sessions']['meta_info']


    class Statistics(object):
        """
        Statistical data pertaining to the NETCONF server.
        
        .. attribute:: dropped_sessions
        
        	Number of sessions that were abnormally terminated, e.g., due to idle timeout or transport close.  This counter is not incremented when a session is properly closed by a <close\-session> operation, or killed by a <kill\-session> operation
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: in_bad_hellos
        
        	Number of sessions silently dropped because an invalid <hello> message was received.  This includes <hello> messages with a 'session\-id' attribute, bad namespace, and bad capability declarations
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: in_bad_rpcs
        
        	Number of messages received when an <rpc> message was expected, that were not correct <rpc> messages.  This includes XML parse errors and errors on the rpc layer
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: in_rpcs
        
        	Number of correct <rpc> messages received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: in_sessions
        
        	Number of sessions started.  This counter is incremented when a <hello> message with a <session\-id> is sent.  'in\-sessions' \- 'in\-bad\-hellos' =    'number of correctly started netconf sessions'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: netconf_start_time
        
        	Date and time at which the management subsystem was started
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: out_notifications
        
        	Number of <notification> messages sent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: out_rpc_errors
        
        	Number of <rpc\-reply> messages sent that contained an <rpc\-error> element
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            self.parent = None
            self.dropped_sessions = None
            self.in_bad_hellos = None
            self.in_bad_rpcs = None
            self.in_rpcs = None
            self.in_sessions = None
            self.netconf_start_time = None
            self.out_notifications = None
            self.out_rpc_errors = None

        @property
        def _common_path(self):

            return '/ietf-netconf-monitoring:netconf-state/ietf-netconf-monitoring:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dropped_sessions is not None:
                return True

            if self.in_bad_hellos is not None:
                return True

            if self.in_bad_rpcs is not None:
                return True

            if self.in_rpcs is not None:
                return True

            if self.in_sessions is not None:
                return True

            if self.netconf_start_time is not None:
                return True

            if self.out_notifications is not None:
                return True

            if self.out_rpc_errors is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
            return meta._meta_table['NetconfState.Statistics']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf-monitoring:netconf-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.capabilities is not None and self.capabilities._has_data():
            return True

        if self.datastores is not None and self.datastores._has_data():
            return True

        if self.schemas is not None and self.schemas._has_data():
            return True

        if self.sessions is not None and self.sessions._has_data():
            return True

        if self.statistics is not None and self.statistics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['NetconfState']['meta_info']


class GetSchemaRpc(object):
    """
    This operation is used to retrieve a schema from the
    NETCONF server.
    
    Positive Response\:
      The NETCONF server returns the requested schema.
    
    Negative Response\:
      If requested schema does not exist, the <error\-tag> is
      'invalid\-value'.
    
      If more than one schema matches the requested parameters, the
      <error\-tag> is 'operation\-failed', and <error\-app\-tag> is
      'data\-not\-unique'.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf_monitoring.GetSchemaRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_netconf_monitoring.GetSchemaRpc.Output>`
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        self.input = GetSchemaRpc.Input()
        self.input.parent = self
        self.output = GetSchemaRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: format
        
        	The data modeling language of the schema.  If this parameter is not present, and more than one formats of the schema exists on the server, a 'data\-not\-unique' error is returned, as described above
        	**type**\:   :py:class:`SchemaFormatIdentity <ydk.models.ietf.ietf_netconf_monitoring.SchemaFormatIdentity>`
        
        .. attribute:: identifier
        
        	Identifier for the schema list entry
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: version
        
        	Version of the schema requested.  If this parameter is not present, and more than one version of the schema exists on the server, a 'data\-not\-unique' error is returned, as described above
        	**type**\:  str
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            self.parent = None
            self.format = None
            self.identifier = None
            self.version = None

        @property
        def _common_path(self):

            return '/ietf-netconf-monitoring:get-schema/ietf-netconf-monitoring:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.format is not None:
                return True

            if self.identifier is not None:
                return True

            if self.version is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
            return meta._meta_table['GetSchemaRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: data
        
        	Contains the schema content
        	**type**\:  anyxml
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            self.parent = None
            self.data = None

        @property
        def _common_path(self):

            return '/ietf-netconf-monitoring:get-schema/ietf-netconf-monitoring:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.data is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
            return meta._meta_table['GetSchemaRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf-monitoring:get-schema'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['GetSchemaRpc']['meta_info']


class NetconfBeepIdentity(TransportIdentity):
    """
    NETCONF over Blocks Extensible Exchange Protocol (BEEP).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['NetconfBeepIdentity']['meta_info']


class RngIdentity(SchemaFormatIdentity):
    """
    Regular Language for XML Next Generation (RELAX NG).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        SchemaFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['RngIdentity']['meta_info']


class XsdIdentity(SchemaFormatIdentity):
    """
    W3C XML Schema Definition.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        SchemaFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['XsdIdentity']['meta_info']


class NetconfSshIdentity(TransportIdentity):
    """
    NETCONF over Secure Shell (SSH).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['NetconfSshIdentity']['meta_info']


class RncIdentity(SchemaFormatIdentity):
    """
    Relax NG Compact Syntax
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        SchemaFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['RncIdentity']['meta_info']


class YinIdentity(SchemaFormatIdentity):
    """
    The YIN syntax for YANG.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        SchemaFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['YinIdentity']['meta_info']


class YangIdentity(SchemaFormatIdentity):
    """
    The YANG data modeling language for NETCONF.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        SchemaFormatIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['YangIdentity']['meta_info']


class NetconfSoapOverHttpsIdentity(TransportIdentity):
    """
    NETCONF over Simple Object Access Protocol (SOAP)
    over Hypertext Transfer Protocol Secure (HTTPS).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['NetconfSoapOverHttpsIdentity']['meta_info']


class NetconfSoapOverBeepIdentity(TransportIdentity):
    """
    NETCONF over Simple Object Access Protocol (SOAP) over
    Blocks Extensible Exchange Protocol (BEEP).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['NetconfSoapOverBeepIdentity']['meta_info']


class NetconfTlsIdentity(TransportIdentity):
    """
    NETCONF over Transport Layer Security (TLS).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_monitoring as meta
        return meta._meta_table['NetconfTlsIdentity']['meta_info']


