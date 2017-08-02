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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class NetconfDatastoreType(Enum):
    """
    NetconfDatastoreType

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


class NetconfState(Entity):
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
        super(NetconfState, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf-state"
        self.yang_parent_name = "ietf-netconf-monitoring"

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


    class Datastores(Entity):
        """
        Contains the list of NETCONF configuration datastores.
        
        .. attribute:: datastore
        
        	List of NETCONF configuration datastores supported by the NETCONF server and related information
        	**type**\: list of    :py:class:`Datastore <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore>`
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(NetconfState.Datastores, self).__init__()

            self.yang_name = "datastores"
            self.yang_parent_name = "netconf-state"

            self.datastore = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NetconfState.Datastores, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetconfState.Datastores, self).__setattr__(name, value)


        class Datastore(Entity):
            """
            List of NETCONF configuration datastores supported by
            the NETCONF server and related information.
            
            .. attribute:: name  <key>
            
            	Name of the datastore associated with this list entry
            	**type**\:   :py:class:`NetconfDatastoreType <ydk.models.ietf.ietf_netconf_monitoring.NetconfDatastoreType>`
            
            .. attribute:: locks
            
            	The NETCONF <lock> and <partial\-lock> operations allow a client to lock specific resources in a datastore.  The NETCONF server will prevent changes to the locked resources by all sessions except the one that acquired the lock(s).  Monitoring information is provided for each datastore entry including details such as the session that acquired the lock, the type of lock (global or partial) and the list of locked resources.  Multiple locks per datastore are supported
            	**type**\:   :py:class:`Locks <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ncm'
            _revision = '2010-10-04'

            def __init__(self):
                super(NetconfState.Datastores.Datastore, self).__init__()

                self.yang_name = "datastore"
                self.yang_parent_name = "datastores"

                self.name = YLeaf(YType.enumeration, "name")

                self.locks = None
                self._children_name_map["locks"] = "locks"
                self._children_yang_names.add("locks")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfState.Datastores.Datastore, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfState.Datastores.Datastore, self).__setattr__(name, value)


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
                	**type**\:   :py:class:`GlobalLock <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks.GlobalLock>`
                
                .. attribute:: partial_lock
                
                	List of partial locks
                	**type**\: list of    :py:class:`PartialLock <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Datastores.Datastore.Locks.PartialLock>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ncm'
                _revision = '2010-10-04'

                def __init__(self):
                    super(NetconfState.Datastores.Datastore.Locks, self).__init__()

                    self.yang_name = "locks"
                    self.yang_parent_name = "datastore"
                    self.is_presence_container = True

                    self.global_lock = NetconfState.Datastores.Datastore.Locks.GlobalLock()
                    self.global_lock.parent = self
                    self._children_name_map["global_lock"] = "global-lock"
                    self._children_yang_names.add("global-lock")

                    self.partial_lock = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetconfState.Datastores.Datastore.Locks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetconfState.Datastores.Datastore.Locks, self).__setattr__(name, value)


                class GlobalLock(Entity):
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
                        super(NetconfState.Datastores.Datastore.Locks.GlobalLock, self).__init__()

                        self.yang_name = "global-lock"
                        self.yang_parent_name = "locks"

                        self.locked_by_session = YLeaf(YType.uint32, "locked-by-session")

                        self.locked_time = YLeaf(YType.str, "locked-time")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("locked_by_session",
                                        "locked_time") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NetconfState.Datastores.Datastore.Locks.GlobalLock, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NetconfState.Datastores.Datastore.Locks.GlobalLock, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.locked_by_session.is_set or
                            self.locked_time.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.locked_by_session.yfilter != YFilter.not_set or
                            self.locked_time.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "global-lock" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.locked_by_session.is_set or self.locked_by_session.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.locked_by_session.get_name_leafdata())
                        if (self.locked_time.is_set or self.locked_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.locked_time.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "locked-by-session" or name == "locked-time"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "locked-by-session"):
                            self.locked_by_session = value
                            self.locked_by_session.value_namespace = name_space
                            self.locked_by_session.value_namespace_prefix = name_space_prefix
                        if(value_path == "locked-time"):
                            self.locked_time = value
                            self.locked_time.value_namespace = name_space
                            self.locked_time.value_namespace_prefix = name_space_prefix


                class PartialLock(Entity):
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
                        super(NetconfState.Datastores.Datastore.Locks.PartialLock, self).__init__()

                        self.yang_name = "partial-lock"
                        self.yang_parent_name = "locks"

                        self.lock_id = YLeaf(YType.uint32, "lock-id")

                        self.locked_by_session = YLeaf(YType.uint32, "locked-by-session")

                        self.locked_node = YLeafList(YType.str, "locked-node")

                        self.locked_time = YLeaf(YType.str, "locked-time")

                        self.select = YLeafList(YType.str, "select")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("lock_id",
                                        "locked_by_session",
                                        "locked_node",
                                        "locked_time",
                                        "select") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(NetconfState.Datastores.Datastore.Locks.PartialLock, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(NetconfState.Datastores.Datastore.Locks.PartialLock, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.locked_node.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        for leaf in self.select.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.lock_id.is_set or
                            self.locked_by_session.is_set or
                            self.locked_time.is_set)

                    def has_operation(self):
                        for leaf in self.locked_node.getYLeafs():
                            if (leaf.is_set):
                                return True
                        for leaf in self.select.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.lock_id.yfilter != YFilter.not_set or
                            self.locked_by_session.yfilter != YFilter.not_set or
                            self.locked_node.yfilter != YFilter.not_set or
                            self.locked_time.yfilter != YFilter.not_set or
                            self.select.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "partial-lock" + "[lock-id='" + self.lock_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.lock_id.is_set or self.lock_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lock_id.get_name_leafdata())
                        if (self.locked_by_session.is_set or self.locked_by_session.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.locked_by_session.get_name_leafdata())
                        if (self.locked_time.is_set or self.locked_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.locked_time.get_name_leafdata())

                        leaf_name_data.extend(self.locked_node.get_name_leafdata())

                        leaf_name_data.extend(self.select.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "lock-id" or name == "locked-by-session" or name == "locked-node" or name == "locked-time" or name == "select"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "lock-id"):
                            self.lock_id = value
                            self.lock_id.value_namespace = name_space
                            self.lock_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "locked-by-session"):
                            self.locked_by_session = value
                            self.locked_by_session.value_namespace = name_space
                            self.locked_by_session.value_namespace_prefix = name_space_prefix
                        if(value_path == "locked-node"):
                            self.locked_node.append(value)
                        if(value_path == "locked-time"):
                            self.locked_time = value
                            self.locked_time.value_namespace = name_space
                            self.locked_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "select"):
                            self.select.append(value)

                def has_data(self):
                    for c in self.partial_lock:
                        if (c.has_data()):
                            return True
                    return (self.global_lock is not None and self.global_lock.has_data())

                def has_operation(self):
                    for c in self.partial_lock:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.global_lock is not None and self.global_lock.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "locks" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "global-lock"):
                        if (self.global_lock is None):
                            self.global_lock = NetconfState.Datastores.Datastore.Locks.GlobalLock()
                            self.global_lock.parent = self
                            self._children_name_map["global_lock"] = "global-lock"
                        return self.global_lock

                    if (child_yang_name == "partial-lock"):
                        for c in self.partial_lock:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = NetconfState.Datastores.Datastore.Locks.PartialLock()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.partial_lock.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "global-lock" or name == "partial-lock"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.locks is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.locks is not None and self.locks.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "datastore" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf-monitoring:netconf-state/datastores/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "locks"):
                    if (self.locks is None):
                        self.locks = NetconfState.Datastores.Datastore.Locks()
                        self.locks.parent = self
                        self._children_name_map["locks"] = "locks"
                    return self.locks

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "locks" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.datastore:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.datastore:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "datastores" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf-monitoring:netconf-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "datastore"):
                for c in self.datastore:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfState.Datastores.Datastore()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.datastore.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "datastore"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Statistics(Entity):
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
            super(NetconfState.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "netconf-state"

            self.dropped_sessions = YLeaf(YType.uint32, "dropped-sessions")

            self.in_bad_hellos = YLeaf(YType.uint32, "in-bad-hellos")

            self.in_bad_rpcs = YLeaf(YType.uint32, "in-bad-rpcs")

            self.in_rpcs = YLeaf(YType.uint32, "in-rpcs")

            self.in_sessions = YLeaf(YType.uint32, "in-sessions")

            self.netconf_start_time = YLeaf(YType.str, "netconf-start-time")

            self.out_notifications = YLeaf(YType.uint32, "out-notifications")

            self.out_rpc_errors = YLeaf(YType.uint32, "out-rpc-errors")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("dropped_sessions",
                            "in_bad_hellos",
                            "in_bad_rpcs",
                            "in_rpcs",
                            "in_sessions",
                            "netconf_start_time",
                            "out_notifications",
                            "out_rpc_errors") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NetconfState.Statistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetconfState.Statistics, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.dropped_sessions.is_set or
                self.in_bad_hellos.is_set or
                self.in_bad_rpcs.is_set or
                self.in_rpcs.is_set or
                self.in_sessions.is_set or
                self.netconf_start_time.is_set or
                self.out_notifications.is_set or
                self.out_rpc_errors.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.dropped_sessions.yfilter != YFilter.not_set or
                self.in_bad_hellos.yfilter != YFilter.not_set or
                self.in_bad_rpcs.yfilter != YFilter.not_set or
                self.in_rpcs.yfilter != YFilter.not_set or
                self.in_sessions.yfilter != YFilter.not_set or
                self.netconf_start_time.yfilter != YFilter.not_set or
                self.out_notifications.yfilter != YFilter.not_set or
                self.out_rpc_errors.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "statistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf-monitoring:netconf-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.dropped_sessions.is_set or self.dropped_sessions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dropped_sessions.get_name_leafdata())
            if (self.in_bad_hellos.is_set or self.in_bad_hellos.yfilter != YFilter.not_set):
                leaf_name_data.append(self.in_bad_hellos.get_name_leafdata())
            if (self.in_bad_rpcs.is_set or self.in_bad_rpcs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.in_bad_rpcs.get_name_leafdata())
            if (self.in_rpcs.is_set or self.in_rpcs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.in_rpcs.get_name_leafdata())
            if (self.in_sessions.is_set or self.in_sessions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.in_sessions.get_name_leafdata())
            if (self.netconf_start_time.is_set or self.netconf_start_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.netconf_start_time.get_name_leafdata())
            if (self.out_notifications.is_set or self.out_notifications.yfilter != YFilter.not_set):
                leaf_name_data.append(self.out_notifications.get_name_leafdata())
            if (self.out_rpc_errors.is_set or self.out_rpc_errors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.out_rpc_errors.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dropped-sessions" or name == "in-bad-hellos" or name == "in-bad-rpcs" or name == "in-rpcs" or name == "in-sessions" or name == "netconf-start-time" or name == "out-notifications" or name == "out-rpc-errors"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "dropped-sessions"):
                self.dropped_sessions = value
                self.dropped_sessions.value_namespace = name_space
                self.dropped_sessions.value_namespace_prefix = name_space_prefix
            if(value_path == "in-bad-hellos"):
                self.in_bad_hellos = value
                self.in_bad_hellos.value_namespace = name_space
                self.in_bad_hellos.value_namespace_prefix = name_space_prefix
            if(value_path == "in-bad-rpcs"):
                self.in_bad_rpcs = value
                self.in_bad_rpcs.value_namespace = name_space
                self.in_bad_rpcs.value_namespace_prefix = name_space_prefix
            if(value_path == "in-rpcs"):
                self.in_rpcs = value
                self.in_rpcs.value_namespace = name_space
                self.in_rpcs.value_namespace_prefix = name_space_prefix
            if(value_path == "in-sessions"):
                self.in_sessions = value
                self.in_sessions.value_namespace = name_space
                self.in_sessions.value_namespace_prefix = name_space_prefix
            if(value_path == "netconf-start-time"):
                self.netconf_start_time = value
                self.netconf_start_time.value_namespace = name_space
                self.netconf_start_time.value_namespace_prefix = name_space_prefix
            if(value_path == "out-notifications"):
                self.out_notifications = value
                self.out_notifications.value_namespace = name_space
                self.out_notifications.value_namespace_prefix = name_space_prefix
            if(value_path == "out-rpc-errors"):
                self.out_rpc_errors = value
                self.out_rpc_errors.value_namespace = name_space
                self.out_rpc_errors.value_namespace_prefix = name_space_prefix


    class Schemas(Entity):
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
            super(NetconfState.Schemas, self).__init__()

            self.yang_name = "schemas"
            self.yang_parent_name = "netconf-state"

            self.schema = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NetconfState.Schemas, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetconfState.Schemas, self).__setattr__(name, value)


        class Schema(Entity):
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
            	**type**\:   :py:class:`SchemaFormat <ydk.models.ietf.ietf_netconf_monitoring.SchemaFormat>`
            
            .. attribute:: location
            
            	One or more locations from which the schema can be retrieved.  This list SHOULD contain at least one entry per schema.  A schema entry may be located on a remote file system (e.g., reference to file system for ftp retrieval) or retrieved directly from a server supporting the <get\-schema> operation (denoted by the value 'NETCONF')
            	**type**\: one of the below types:
            
            	**type**\:  list of   :py:class:`Location <ydk.models.ietf.ietf_netconf_monitoring.NetconfState.Schemas.Schema.Location>`
            
            
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
                super(NetconfState.Schemas.Schema, self).__init__()

                self.yang_name = "schema"
                self.yang_parent_name = "schemas"

                self.identifier = YLeaf(YType.str, "identifier")

                self.version = YLeaf(YType.str, "version")

                self.format = YLeaf(YType.identityref, "format")

                self.location = YLeafList(YType.str, "location")

                self.namespace = YLeaf(YType.str, "namespace")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("identifier",
                                "version",
                                "format",
                                "location",
                                "namespace") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfState.Schemas.Schema, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfState.Schemas.Schema, self).__setattr__(name, value)

            class Location(Enum):
                """
                Location

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


            def has_data(self):
                for leaf in self.location.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.identifier.is_set or
                    self.version.is_set or
                    self.format.is_set or
                    self.namespace.is_set)

            def has_operation(self):
                for leaf in self.location.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.identifier.yfilter != YFilter.not_set or
                    self.version.yfilter != YFilter.not_set or
                    self.format.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set or
                    self.namespace.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "schema" + "[identifier='" + self.identifier.get() + "']" + "[version='" + self.version.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf-monitoring:netconf-state/schemas/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.identifier.is_set or self.identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.identifier.get_name_leafdata())
                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.version.get_name_leafdata())
                if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.format.get_name_leafdata())
                if (self.namespace.is_set or self.namespace.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.namespace.get_name_leafdata())

                leaf_name_data.extend(self.location.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "identifier" or name == "version" or name == "format" or name == "location" or name == "namespace"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "identifier"):
                    self.identifier = value
                    self.identifier.value_namespace = name_space
                    self.identifier.value_namespace_prefix = name_space_prefix
                if(value_path == "version"):
                    self.version = value
                    self.version.value_namespace = name_space
                    self.version.value_namespace_prefix = name_space_prefix
                if(value_path == "format"):
                    self.format = value
                    self.format.value_namespace = name_space
                    self.format.value_namespace_prefix = name_space_prefix
                if(value_path == "location"):
                    self.location.append(value)
                if(value_path == "namespace"):
                    self.namespace = value
                    self.namespace.value_namespace = name_space
                    self.namespace.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.schema:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.schema:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "schemas" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf-monitoring:netconf-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "schema"):
                for c in self.schema:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfState.Schemas.Schema()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.schema.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "schema"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Capabilities(Entity):
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
            super(NetconfState.Capabilities, self).__init__()

            self.yang_name = "capabilities"
            self.yang_parent_name = "netconf-state"

            self.capability = YLeafList(YType.str, "capability")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("capability") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NetconfState.Capabilities, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetconfState.Capabilities, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.capability.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return False

        def has_operation(self):
            for leaf in self.capability.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.capability.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "capabilities" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf-monitoring:netconf-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            leaf_name_data.extend(self.capability.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "capability"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "capability"):
                self.capability.append(value)


    class Sessions(Entity):
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
            super(NetconfState.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "netconf-state"

            self.session = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NetconfState.Sessions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetconfState.Sessions, self).__setattr__(name, value)


        class Session(Entity):
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
            	**type**\:   :py:class:`Transport <ydk.models.ietf.ietf_netconf_monitoring.Transport>`
            
            	**mandatory**\: True
            
            .. attribute:: username
            
            	The username is the client identity that was authenticated by the NETCONF transport protocol.  The algorithm used to derive the username is NETCONF transport protocol specific and in addition specific to the authentication mechanism used by the NETCONF transport protocol
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ncm'
            _revision = '2010-10-04'

            def __init__(self):
                super(NetconfState.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"

                self.session_id = YLeaf(YType.uint32, "session-id")

                self.in_bad_rpcs = YLeaf(YType.uint32, "in-bad-rpcs")

                self.in_rpcs = YLeaf(YType.uint32, "in-rpcs")

                self.login_time = YLeaf(YType.str, "login-time")

                self.out_notifications = YLeaf(YType.uint32, "out-notifications")

                self.out_rpc_errors = YLeaf(YType.uint32, "out-rpc-errors")

                self.source_host = YLeaf(YType.str, "source-host")

                self.transport = YLeaf(YType.identityref, "transport")

                self.username = YLeaf(YType.str, "username")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("session_id",
                                "in_bad_rpcs",
                                "in_rpcs",
                                "login_time",
                                "out_notifications",
                                "out_rpc_errors",
                                "source_host",
                                "transport",
                                "username") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfState.Sessions.Session, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfState.Sessions.Session, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.session_id.is_set or
                    self.in_bad_rpcs.is_set or
                    self.in_rpcs.is_set or
                    self.login_time.is_set or
                    self.out_notifications.is_set or
                    self.out_rpc_errors.is_set or
                    self.source_host.is_set or
                    self.transport.is_set or
                    self.username.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.session_id.yfilter != YFilter.not_set or
                    self.in_bad_rpcs.yfilter != YFilter.not_set or
                    self.in_rpcs.yfilter != YFilter.not_set or
                    self.login_time.yfilter != YFilter.not_set or
                    self.out_notifications.yfilter != YFilter.not_set or
                    self.out_rpc_errors.yfilter != YFilter.not_set or
                    self.source_host.yfilter != YFilter.not_set or
                    self.transport.yfilter != YFilter.not_set or
                    self.username.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "session" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-netconf-monitoring:netconf-state/sessions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_id.get_name_leafdata())
                if (self.in_bad_rpcs.is_set or self.in_bad_rpcs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_bad_rpcs.get_name_leafdata())
                if (self.in_rpcs.is_set or self.in_rpcs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_rpcs.get_name_leafdata())
                if (self.login_time.is_set or self.login_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.login_time.get_name_leafdata())
                if (self.out_notifications.is_set or self.out_notifications.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_notifications.get_name_leafdata())
                if (self.out_rpc_errors.is_set or self.out_rpc_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_rpc_errors.get_name_leafdata())
                if (self.source_host.is_set or self.source_host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_host.get_name_leafdata())
                if (self.transport.is_set or self.transport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transport.get_name_leafdata())
                if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.username.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "session-id" or name == "in-bad-rpcs" or name == "in-rpcs" or name == "login-time" or name == "out-notifications" or name == "out-rpc-errors" or name == "source-host" or name == "transport" or name == "username"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "session-id"):
                    self.session_id = value
                    self.session_id.value_namespace = name_space
                    self.session_id.value_namespace_prefix = name_space_prefix
                if(value_path == "in-bad-rpcs"):
                    self.in_bad_rpcs = value
                    self.in_bad_rpcs.value_namespace = name_space
                    self.in_bad_rpcs.value_namespace_prefix = name_space_prefix
                if(value_path == "in-rpcs"):
                    self.in_rpcs = value
                    self.in_rpcs.value_namespace = name_space
                    self.in_rpcs.value_namespace_prefix = name_space_prefix
                if(value_path == "login-time"):
                    self.login_time = value
                    self.login_time.value_namespace = name_space
                    self.login_time.value_namespace_prefix = name_space_prefix
                if(value_path == "out-notifications"):
                    self.out_notifications = value
                    self.out_notifications.value_namespace = name_space
                    self.out_notifications.value_namespace_prefix = name_space_prefix
                if(value_path == "out-rpc-errors"):
                    self.out_rpc_errors = value
                    self.out_rpc_errors.value_namespace = name_space
                    self.out_rpc_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "source-host"):
                    self.source_host = value
                    self.source_host.value_namespace = name_space
                    self.source_host.value_namespace_prefix = name_space_prefix
                if(value_path == "transport"):
                    self.transport = value
                    self.transport.value_namespace = name_space
                    self.transport.value_namespace_prefix = name_space_prefix
                if(value_path == "username"):
                    self.username = value
                    self.username.value_namespace = name_space
                    self.username.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.session:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.session:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sessions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf-monitoring:netconf-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "session"):
                for c in self.session:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfState.Sessions.Session()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.session.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "session"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.capabilities is not None and self.capabilities.has_data()) or
            (self.datastores is not None and self.datastores.has_data()) or
            (self.schemas is not None and self.schemas.has_data()) or
            (self.sessions is not None and self.sessions.has_data()) or
            (self.statistics is not None and self.statistics.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.capabilities is not None and self.capabilities.has_operation()) or
            (self.datastores is not None and self.datastores.has_operation()) or
            (self.schemas is not None and self.schemas.has_operation()) or
            (self.sessions is not None and self.sessions.has_operation()) or
            (self.statistics is not None and self.statistics.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf-monitoring:netconf-state" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "capabilities"):
            if (self.capabilities is None):
                self.capabilities = NetconfState.Capabilities()
                self.capabilities.parent = self
                self._children_name_map["capabilities"] = "capabilities"
            return self.capabilities

        if (child_yang_name == "datastores"):
            if (self.datastores is None):
                self.datastores = NetconfState.Datastores()
                self.datastores.parent = self
                self._children_name_map["datastores"] = "datastores"
            return self.datastores

        if (child_yang_name == "schemas"):
            if (self.schemas is None):
                self.schemas = NetconfState.Schemas()
                self.schemas.parent = self
                self._children_name_map["schemas"] = "schemas"
            return self.schemas

        if (child_yang_name == "sessions"):
            if (self.sessions is None):
                self.sessions = NetconfState.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
            return self.sessions

        if (child_yang_name == "statistics"):
            if (self.statistics is None):
                self.statistics = NetconfState.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
            return self.statistics

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "capabilities" or name == "datastores" or name == "schemas" or name == "sessions" or name == "statistics"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NetconfState()
        return self._top_entity

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
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_netconf_monitoring.GetSchema.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_netconf_monitoring.GetSchema.Output>`
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(GetSchema, self).__init__()
        self._top_entity = None

        self.yang_name = "get-schema"
        self.yang_parent_name = "ietf-netconf-monitoring"

        self.input = GetSchema.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = GetSchema.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: format
        
        	The data modeling language of the schema.  If this parameter is not present, and more than one formats of the schema exists on the server, a 'data\-not\-unique' error is returned, as described above
        	**type**\:   :py:class:`SchemaFormat <ydk.models.ietf.ietf_netconf_monitoring.SchemaFormat>`
        
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
            super(GetSchema.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "get-schema"

            self.format = YLeaf(YType.identityref, "format")

            self.identifier = YLeaf(YType.str, "identifier")

            self.version = YLeaf(YType.str, "version")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("format",
                            "identifier",
                            "version") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(GetSchema.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(GetSchema.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.format.is_set or
                self.identifier.is_set or
                self.version.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.format.yfilter != YFilter.not_set or
                self.identifier.yfilter != YFilter.not_set or
                self.version.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf-monitoring:get-schema/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                leaf_name_data.append(self.format.get_name_leafdata())
            if (self.identifier.is_set or self.identifier.yfilter != YFilter.not_set):
                leaf_name_data.append(self.identifier.get_name_leafdata())
            if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                leaf_name_data.append(self.version.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "format" or name == "identifier" or name == "version"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "format"):
                self.format = value
                self.format.value_namespace = name_space
                self.format.value_namespace_prefix = name_space_prefix
            if(value_path == "identifier"):
                self.identifier = value
                self.identifier.value_namespace = name_space
                self.identifier.value_namespace_prefix = name_space_prefix
            if(value_path == "version"):
                self.version = value
                self.version.value_namespace = name_space
                self.version.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: data
        
        	Contains the schema content
        	**type**\:  anyxml
        
        

        """

        _prefix = 'ncm'
        _revision = '2010-10-04'

        def __init__(self):
            super(GetSchema.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "get-schema"

            self.data = YLeaf(YType.str, "data")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("data") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(GetSchema.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(GetSchema.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.data.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.data.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-netconf-monitoring:get-schema/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.data.is_set or self.data.yfilter != YFilter.not_set):
                leaf_name_data.append(self.data.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "data"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "data"):
                self.data = value
                self.data.value_namespace = name_space
                self.data.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-netconf-monitoring:get-schema" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = GetSchema.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = GetSchema.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = GetSchema()
        return self._top_entity

class NetconfSoapOverBeep(Identity):
    """
    NETCONF over Simple Object Access Protocol (SOAP) over
    Blocks Extensible Exchange Protocol (BEEP).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfSoapOverBeep, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-soap-over-beep")


class NetconfTls(Identity):
    """
    NETCONF over Transport Layer Security (TLS).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfTls, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-tls")


class NetconfSoapOverHttps(Identity):
    """
    NETCONF over Simple Object Access Protocol (SOAP)
    over Hypertext Transfer Protocol Secure (HTTPS).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfSoapOverHttps, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-soap-over-https")


class Xsd(Identity):
    """
    W3C XML Schema Definition.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Xsd, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:xsd")


class Rnc(Identity):
    """
    Relax NG Compact Syntax
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Rnc, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:rnc")


class NetconfBeep(Identity):
    """
    NETCONF over Blocks Extensible Exchange Protocol (BEEP).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfBeep, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-beep")


class Yin(Identity):
    """
    The YIN syntax for YANG.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Yin, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:yin")


class NetconfSsh(Identity):
    """
    NETCONF over Secure Shell (SSH).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(NetconfSsh, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:netconf-ssh")


class Yang(Identity):
    """
    The YANG data modeling language for NETCONF.
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Yang, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:yang")


class Rng(Identity):
    """
    Regular Language for XML Next Generation (RELAX NG).
    
    

    """

    _prefix = 'ncm'
    _revision = '2010-10-04'

    def __init__(self):
        super(Rng, self).__init__("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring", "ietf-netconf-monitoring", "ietf-netconf-monitoring:rng")


