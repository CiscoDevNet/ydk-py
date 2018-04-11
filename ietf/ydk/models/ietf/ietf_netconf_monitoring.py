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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class NetconfDatastoreType(Enum):
    """
    NetconfDatastoreType (Enum Class)

    Enumeration of possible NETCONF datastore types.

    .. data:: running = 0

    .. data:: candidate = 1

    .. data:: startup = 2

    """

    running = Enum.YLeaf(0, "running")

    candidate = Enum.YLeaf(1, "candidate")

    startup = Enum.YLeaf(2, "startup")



class Transport(Identity):
    """
    Base identity for NETCONF transport types.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Transport, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:transport")


class SchemaFormat(Identity):
    """
    Base identity for data model schema languages.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(SchemaFormat, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:schema-format")


class GetSchema(Entity):
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
    
    	
    	**type**\:  :py:class:`Input <ydk.models.ietf.ietf_netconf_monitoring.GetSchema.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.ietf.ietf_netconf_monitoring.GetSchema.Output>`
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(GetSchema, self).__init__()
        self._top_entity = None

        self.yang_name = "get-schema"
        self.yang_parent_name = "ietf-netconf-monitoring"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = GetSchema.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = GetSchema.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "ietf-netconf-monitoring:get-schema"


    class Input(Entity):
        """
        
        
        .. attribute:: identifier
        
        	Identifier for the schema list entry
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: version
        
        	Version of the schema requested.  If this parameter is not present, and more than one version of the schema exists on the server, a 'data\-not\-unique' error is returned, as described above
        	**type**\: str
        
        .. attribute:: format
        
        	The data modeling language of the schema.  If this parameter is not present, and more than one formats of the schema exists on the server, a 'data\-not\-unique' error is returned, as described above
        	**type**\:  :py:class:`SchemaFormat <ydk.models.ietf.ietf_netconf_monitoring.SchemaFormat>`
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(GetSchema.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "get-schema"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('identifier', YLeaf(YType.str, 'identifier')),
                ('version', YLeaf(YType.str, 'version')),
                ('format', YLeaf(YType.identityref, 'format')),
            ])
            self.identifier = None
            self.version = None
            self.format = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "ietf-netconf-monitoring:get-schema/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(GetSchema.Input, ['identifier', 'version', 'format'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: data
        
        	Contains the schema content
        	**type**\: anyxml
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(GetSchema.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "get-schema"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('data', YLeaf(YType.str, 'data')),
            ])
            self.data = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "ietf-netconf-monitoring:get-schema/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(GetSchema.Output, ['data'], name, value)

    def clone_ptr(self):
        self._top_entity = GetSchema()
        return self._top_entity

class NetconfState(Entity):
    """
    The netconf\-state container is the root of the monitoring
    data model.
    
    .. attribute:: capabilities
    
    	Contains the list of NETCONF capabilities supported by the server
    	**type**\:  :py:class:`Capabilities <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Capabilities>`
    
    .. attribute:: datastores
    
    	Contains the list of NETCONF configuration datastores
    	**type**\:  :py:class:`Datastores <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores>`
    
    .. attribute:: schemas
    
    	Contains the list of data model schemas supported by the server
    	**type**\:  :py:class:`Schemas <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Schemas>`
    
    .. attribute:: sessions
    
    	The sessions container includes session\-specific data for NETCONF management sessions.  The session list MUST include all currently active NETCONF sessions
    	**type**\:  :py:class:`Sessions <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Sessions>`
    
    .. attribute:: statistics
    
    	Statistical data pertaining to the NETCONF server
    	**type**\:  :py:class:`Statistics <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Statistics>`
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfState, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf-state"
        self.yang_parent_name = "ietf-netconf-monitoring"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("capabilities", ("capabilities", NetconfState.Capabilities)), ("datastores", ("datastores", NetconfState.Datastores)), ("schemas", ("schemas", NetconfState.Schemas)), ("sessions", ("sessions", NetconfState.Sessions)), ("statistics", ("statistics", NetconfState.Statistics))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.capabilities = NetconfState.Capabilities()
        self.capabilities.parent = self
        self._children_name_map["capabilities"] = "capabilities"
        self._children_yang_names.add("capabilities")

        self.datastores = NetconfState.Datastores()
        self.datastores.parent = self
        self._children_name_map["datastores"] = "datastores"
        self._children_yang_names.add("datastores")

        self.schemas = NetconfState.Schemas()
        self.schemas.parent = self
        self._children_name_map["schemas"] = "schemas"
        self._children_yang_names.add("schemas")

        self.sessions = NetconfState.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")

        self.statistics = NetconfState.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")
        self._segment_path = lambda: "ietf-netconf-monitoring:netconf-state"


    class Capabilities(Entity):
        """
        Contains the list of NETCONF capabilities supported by the
        server.
        
        .. attribute:: capability
        
        	List of NETCONF capabilities supported by the server
        	**type**\: list of str
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(NetconfState.Capabilities, self).__init__()

            self.yang_name = "capabilities"
            self.yang_parent_name = "netconf-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('capability', YLeafList(YType.str, 'capability')),
            ])
            self.capability = []
            self._segment_path = lambda: "capabilities"
            self._absolute_path = lambda: "ietf-netconf-monitoring:netconf-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetconfState.Capabilities, ['capability'], name, value)


    class Datastores(Entity):
        """
        Contains the list of NETCONF configuration datastores.
        
        .. attribute:: datastore
        
        	List of NETCONF configuration datastores supported by the NETCONF server and related information
        	**type**\: list of  		 :py:class:`Datastore <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore>`
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(NetconfState.Datastores, self).__init__()

            self.yang_name = "datastores"
            self.yang_parent_name = "netconf-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("datastore", ("datastore", NetconfState.Datastores.Datastore))])
            self._leafs = OrderedDict()

            self.datastore = YList(self)
            self._segment_path = lambda: "datastores"
            self._absolute_path = lambda: "ietf-netconf-monitoring:netconf-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetconfState.Datastores, [], name, value)


        class Datastore(Entity):
            """
            List of NETCONF configuration datastores supported by
            the NETCONF server and related information.
            
            .. attribute:: name  (key)
            
            	Name of the datastore associated with this list entry
            	**type**\:  :py:class:`NetconfDatastoreType <ydk.models.ietf.ietf_netconf_monitoring.NetconfDatastoreType>`
            
            .. attribute:: locks
            
            	The NETCONF <lock> and <partial\-lock> operations allow a client to lock specific resources in a datastore.  The NETCONF server will prevent changes to the locked resources by all sessions except the one that acquired the lock(s).  Monitoring information is provided for each datastore entry including details such as the session that acquired the lock, the type of lock (global or partial) and the list of locked resources.  Multiple locks per datastore are supported
            	**type**\:  :py:class:`Locks <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ncm'
            _revision = '2010-10-04'

            def __init__(self):
                super(NetconfState.Datastores.Datastore, self).__init__()

                self.yang_name = "datastore"
                self.yang_parent_name = "datastores"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([("locks", ("locks", NetconfState.Datastores.Datastore.Locks))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.enumeration, 'name')),
                ])
                self.name = None

                self.locks = None
                self._children_name_map["locks"] = "locks"
                self._children_yang_names.add("locks")
                self._segment_path = lambda: "datastore" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "ietf-netconf-monitoring:netconf-state/datastores/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfState.Datastores.Datastore, ['name'], name, value)


            class Locks(Entity):
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
                	**type**\:  :py:class:`GlobalLock <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks.GlobalLock>`
                
                .. attribute:: partial_lock
                
                	List of partial locks
                	**type**\: list of  		 :py:class:`PartialLock <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks.PartialLock>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ncm'
                _revision = '2010-10-04'

                def __init__(self):
                    super(NetconfState.Datastores.Datastore.Locks, self).__init__()

                    self.yang_name = "locks"
                    self.yang_parent_name = "datastore"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("global-lock", ("global_lock", NetconfState.Datastores.Datastore.Locks.GlobalLock))])
                    self._child_list_classes = OrderedDict([("partial-lock", ("partial_lock", NetconfState.Datastores.Datastore.Locks.PartialLock))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict()

                    self.global_lock = NetconfState.Datastores.Datastore.Locks.GlobalLock()
                    self.global_lock.parent = self
                    self._children_name_map["global_lock"] = "global-lock"
                    self._children_yang_names.add("global-lock")

                    self.partial_lock = YList(self)
                    self._segment_path = lambda: "locks"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetconfState.Datastores.Datastore.Locks, [], name, value)


                class GlobalLock(Entity):
                    """
                    Present if the global lock is set.
                    
                    .. attribute:: locked_by_session
                    
                    	The session ID of the session that has locked this resource.  Both a global lock and a partial lock MUST contain the NETCONF session\-id.  If the lock is held by a session that is not managed by the NETCONF server (e.g., a CLI session), a session id of 0 (zero) is reported
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: locked_time
                    
                    	The date and time of when the resource was locked
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ncm'
                    _revision = '2010-10-04'

                    def __init__(self):
                        super(NetconfState.Datastores.Datastore.Locks.GlobalLock, self).__init__()

                        self.yang_name = "global-lock"
                        self.yang_parent_name = "locks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('locked_by_session', YLeaf(YType.uint32, 'locked-by-session')),
                            ('locked_time', YLeaf(YType.str, 'locked-time')),
                        ])
                        self.locked_by_session = None
                        self.locked_time = None
                        self._segment_path = lambda: "global-lock"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetconfState.Datastores.Datastore.Locks.GlobalLock, ['locked_by_session', 'locked_time'], name, value)


                class PartialLock(Entity):
                    """
                    List of partial locks.
                    
                    .. attribute:: lock_id  (key)
                    
                    	This is the lock id returned in the <partial\-lock> response
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: locked_by_session
                    
                    	The session ID of the session that has locked this resource.  Both a global lock and a partial lock MUST contain the NETCONF session\-id.  If the lock is held by a session that is not managed by the NETCONF server (e.g., a CLI session), a session id of 0 (zero) is reported
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: locked_time
                    
                    	The date and time of when the resource was locked
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    	**mandatory**\: True
                    
                    .. attribute:: select
                    
                    	The xpath expression that was used to request the lock.  The select expression indicates the original intended scope of the lock
                    	**type**\: list of str
                    
                    .. attribute:: locked_node
                    
                    	The list of instance\-identifiers (i.e., the locked nodes).  The scope of the partial lock is defined by the list of locked nodes
                    	**type**\: list of str
                    
                    

                    """

                    _prefix = 'ncm'
                    _revision = '2010-10-04'

                    def __init__(self):
                        super(NetconfState.Datastores.Datastore.Locks.PartialLock, self).__init__()

                        self.yang_name = "partial-lock"
                        self.yang_parent_name = "locks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lock_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lock_id', YLeaf(YType.uint32, 'lock-id')),
                            ('locked_by_session', YLeaf(YType.uint32, 'locked-by-session')),
                            ('locked_time', YLeaf(YType.str, 'locked-time')),
                            ('select', YLeafList(YType.str, 'select')),
                            ('locked_node', YLeafList(YType.str, 'locked-node')),
                        ])
                        self.lock_id = None
                        self.locked_by_session = None
                        self.locked_time = None
                        self.select = []
                        self.locked_node = []
                        self._segment_path = lambda: "partial-lock" + "[lock-id='" + str(self.lock_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetconfState.Datastores.Datastore.Locks.PartialLock, ['lock_id', 'locked_by_session', 'locked_time', 'select', 'locked_node'], name, value)


    class Schemas(Entity):
        """
        Contains the list of data model schemas supported by the
        server.
        
        .. attribute:: schema
        
        	List of data model schemas supported by the server
        	**type**\: list of  		 :py:class:`Schema <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Schemas.Schema>`
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(NetconfState.Schemas, self).__init__()

            self.yang_name = "schemas"
            self.yang_parent_name = "netconf-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("schema", ("schema", NetconfState.Schemas.Schema))])
            self._leafs = OrderedDict()

            self.schema = YList(self)
            self._segment_path = lambda: "schemas"
            self._absolute_path = lambda: "ietf-netconf-monitoring:netconf-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetconfState.Schemas, [], name, value)


        class Schema(Entity):
            """
            List of data model schemas supported by the server.
            
            .. attribute:: identifier  (key)
            
            	Identifier to uniquely reference the schema.  The identifier is used in the <get\-schema> operation and may be used for other purposes such as file retrieval.  For modeling languages that support or require a data model name (e.g., YANG module name) the identifier MUST match that name.  For YANG data models, the identifier is the name of the module or submodule.  In other cases, an identifier such as a filename MAY be used instead
            	**type**\: str
            
            .. attribute:: version  (key)
            
            	Version of the schema supported.  Multiple versions MAY be supported simultaneously by a NETCONF server.  Each version MUST be reported individually in the schema list, i.e., with same identifier, possibly different location, but different version.  For YANG data models, version is the value of the most recent YANG 'revision' statement in the module or submodule, or the empty string if no 'revision' statement is present
            	**type**\: str
            
            .. attribute:: format  (key)
            
            	The data modeling language the schema is written in (currently xsd, yang, yin, rng, or rnc). For YANG data models, 'yang' format MUST be supported and 'yin' format MAY also be provided
            	**type**\:  :py:class:`SchemaFormat <ydk.models.ietf.ietf_netconf_monitoring.SchemaFormat>`
            
            .. attribute:: namespace
            
            	The XML namespace defined by the data model.  For YANG data models, this is the module's namespace. If the list entry describes a submodule, this field contains the namespace of the module to which the submodule belongs
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: location
            
            	One or more locations from which the schema can be retrieved.  This list SHOULD contain at least one entry per schema.  A schema entry may be located on a remote file system (e.g., reference to file system for ftp retrieval) or retrieved directly from a server supporting the <get\-schema> operation (denoted by the value 'NETCONF')
            	**type**\: union of the below types:
            
            		**type**\: list of   :py:class:`Location <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Schemas.Schema.Location>`
            
            		**type**\: list of str
            
            

            """

            _prefix = 'ncm'
            _revision = '2010-10-04'

            def __init__(self):
                super(NetconfState.Schemas.Schema, self).__init__()

                self.yang_name = "schema"
                self.yang_parent_name = "schemas"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['identifier','version','format']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('identifier', YLeaf(YType.str, 'identifier')),
                    ('version', YLeaf(YType.str, 'version')),
                    ('format', YLeaf(YType.identityref, 'format')),
                    ('namespace', YLeaf(YType.str, 'namespace')),
                    ('location', YLeafList(YType.str, 'location')),
                ])
                self.identifier = None
                self.version = None
                self.format = None
                self.namespace = None
                self.location = []
                self._segment_path = lambda: "schema" + "[identifier='" + str(self.identifier) + "']" + "[version='" + str(self.version) + "']" + "[format='" + str(self.format) + "']"
                self._absolute_path = lambda: "ietf-netconf-monitoring:netconf-state/schemas/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfState.Schemas.Schema, ['identifier', 'version', 'format', 'namespace', 'location'], name, value)

            class Location(Enum):
                """
                Location (Enum Class)

                One or more locations from which the schema can be

                retrieved.  This list SHOULD contain at least one

                entry per schema.

                A schema entry may be located on a remote file system

                (e.g., reference to file system for ftp retrieval) or

                retrieved directly from a server supporting the

                <get\-schema> operation (denoted by the value 'NETCONF').

                .. data:: NETCONF = 0

                """

                NETCONF = Enum.YLeaf(0, "NETCONF")



    class Sessions(Entity):
        """
        The sessions container includes session\-specific data for
        NETCONF management sessions.  The session list MUST include
        all currently active NETCONF sessions.
        
        .. attribute:: session
        
        	All NETCONF sessions managed by the NETCONF server MUST be reported in this list
        	**type**\: list of  		 :py:class:`Session <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Sessions.Session>`
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(NetconfState.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "netconf-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("session", ("session", NetconfState.Sessions.Session))])
            self._leafs = OrderedDict()

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "ietf-netconf-monitoring:netconf-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetconfState.Sessions, [], name, value)


        class Session(Entity):
            """
            All NETCONF sessions managed by the NETCONF server
            MUST be reported in this list.
            
            .. attribute:: session_id  (key)
            
            	Unique identifier for the session.  This value is the NETCONF session identifier, as defined in RFC 4741
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: transport
            
            	Identifies the transport for each session, e.g., 'netconf\-ssh', 'netconf\-soap', etc
            	**type**\:  :py:class:`Transport <ydk.models.ietf.ietf_netconf_monitoring.Transport>`
            
            	**mandatory**\: True
            
            .. attribute:: username
            
            	The username is the client identity that was authenticated by the NETCONF transport protocol.  The algorithm used to derive the username is NETCONF transport protocol specific and in addition specific to the authentication mechanism used by the NETCONF transport protocol
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: source_host
            
            	Host identifier of the NETCONF client.  The value returned is implementation specific (e.g., hostname, IPv4 address, IPv6 address)
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
            
            .. attribute:: login_time
            
            	Time at the server at which the session was established
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**mandatory**\: True
            
            .. attribute:: in_rpcs
            
            	Number of correct <rpc> messages received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_bad_rpcs
            
            	Number of messages received when an <rpc> message was expected, that were not correct <rpc> messages.  This includes XML parse errors and errors on the rpc layer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_rpc_errors
            
            	Number of <rpc\-reply> messages sent that contained an <rpc\-error> element
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_notifications
            
            	Number of <notification> messages sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ncm'
            _revision = '2010-10-04'

            def __init__(self):
                super(NetconfState.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['session_id']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('session_id', YLeaf(YType.uint32, 'session-id')),
                    ('transport', YLeaf(YType.identityref, 'transport')),
                    ('username', YLeaf(YType.str, 'username')),
                    ('source_host', YLeaf(YType.str, 'source-host')),
                    ('login_time', YLeaf(YType.str, 'login-time')),
                    ('in_rpcs', YLeaf(YType.uint32, 'in-rpcs')),
                    ('in_bad_rpcs', YLeaf(YType.uint32, 'in-bad-rpcs')),
                    ('out_rpc_errors', YLeaf(YType.uint32, 'out-rpc-errors')),
                    ('out_notifications', YLeaf(YType.uint32, 'out-notifications')),
                ])
                self.session_id = None
                self.transport = None
                self.username = None
                self.source_host = None
                self.login_time = None
                self.in_rpcs = None
                self.in_bad_rpcs = None
                self.out_rpc_errors = None
                self.out_notifications = None
                self._segment_path = lambda: "session" + "[session-id='" + str(self.session_id) + "']"
                self._absolute_path = lambda: "ietf-netconf-monitoring:netconf-state/sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfState.Sessions.Session, ['session_id', 'transport', 'username', 'source_host', 'login_time', 'in_rpcs', 'in_bad_rpcs', 'out_rpc_errors', 'out_notifications'], name, value)


    class Statistics(Entity):
        """
        Statistical data pertaining to the NETCONF server.
        
        .. attribute:: netconf_start_time
        
        	Date and time at which the management subsystem was started
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: in_bad_hellos
        
        	Number of sessions silently dropped because an invalid <hello> message was received.  This includes <hello> messages with a 'session\-id' attribute, bad namespace, and bad capability declarations
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: in_sessions
        
        	Number of sessions started.  This counter is incremented when a <hello> message with a <session\-id> is sent.  'in\-sessions' \- 'in\-bad\-hellos' =    'number of correctly started netconf sessions'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: dropped_sessions
        
        	Number of sessions that were abnormally terminated, e.g., due to idle timeout or transport close.  This counter is not incremented when a session is properly closed by a <close\-session> operation, or killed by a <kill\-session> operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: in_rpcs
        
        	Number of correct <rpc> messages received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: in_bad_rpcs
        
        	Number of messages received when an <rpc> message was expected, that were not correct <rpc> messages.  This includes XML parse errors and errors on the rpc layer
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: out_rpc_errors
        
        	Number of <rpc\-reply> messages sent that contained an <rpc\-error> element
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: out_notifications
        
        	Number of <notification> messages sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(NetconfState.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "netconf-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('netconf_start_time', YLeaf(YType.str, 'netconf-start-time')),
                ('in_bad_hellos', YLeaf(YType.uint32, 'in-bad-hellos')),
                ('in_sessions', YLeaf(YType.uint32, 'in-sessions')),
                ('dropped_sessions', YLeaf(YType.uint32, 'dropped-sessions')),
                ('in_rpcs', YLeaf(YType.uint32, 'in-rpcs')),
                ('in_bad_rpcs', YLeaf(YType.uint32, 'in-bad-rpcs')),
                ('out_rpc_errors', YLeaf(YType.uint32, 'out-rpc-errors')),
                ('out_notifications', YLeaf(YType.uint32, 'out-notifications')),
            ])
            self.netconf_start_time = None
            self.in_bad_hellos = None
            self.in_sessions = None
            self.dropped_sessions = None
            self.in_rpcs = None
            self.in_bad_rpcs = None
            self.out_rpc_errors = None
            self.out_notifications = None
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "ietf-netconf-monitoring:netconf-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetconfState.Statistics, ['netconf_start_time', 'in_bad_hellos', 'in_sessions', 'dropped_sessions', 'in_rpcs', 'in_bad_rpcs', 'out_rpc_errors', 'out_notifications'], name, value)

    def clone_ptr(self):
        self._top_entity = NetconfState()
        return self._top_entity

class NetconfSsh(Identity):
    """
    NETCONF over Secure Shell (SSH).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfSsh, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-ssh")


class NetconfSoapOverBeep(Identity):
    """
    NETCONF over Simple Object Access Protocol (SOAP) over
    Blocks Extensible Exchange Protocol (BEEP).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfSoapOverBeep, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-soap-over-beep")


class NetconfSoapOverHttps(Identity):
    """
    NETCONF over Simple Object Access Protocol (SOAP)
    over Hypertext Transfer Protocol Secure (HTTPS).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfSoapOverHttps, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-soap-over-https")


class NetconfBeep(Identity):
    """
    NETCONF over Blocks Extensible Exchange Protocol (BEEP).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfBeep, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-beep")


class NetconfTls(Identity):
    """
    NETCONF over Transport Layer Security (TLS).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfTls, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-tls")


class Xsd(Identity):
    """
    W3C XML Schema Definition.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Xsd, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:xsd")


class Yang(Identity):
    """
    The YANG data modeling language for NETCONF.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Yang, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:yang")


class Yin(Identity):
    """
    The YIN syntax for YANG.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Yin, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:yin")


class Rng(Identity):
    """
    Regular Language for XML Next Generation (RELAX NG).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Rng, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:rng")


class Rnc(Identity):
    """
    Relax NG Compact Syntax
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Rnc, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:rnc")


