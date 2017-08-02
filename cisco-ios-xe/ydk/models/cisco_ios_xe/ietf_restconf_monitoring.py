""" ietf_restconf_monitoring 

This module contains monitoring information for the
RESTCONF protocol.

Copyright (c) 2016 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RestconfState(Entity):
    """
    Contains RESTCONF protocol monitoring information.
    
    .. attribute:: capabilities
    
    	Contains a list of protocol capability URIs
    	**type**\:   :py:class:`Capabilities <ydk.models.ietf.ietf_restconf_monitoring.RestconfState.Capabilities>`
    
    .. attribute:: streams
    
    	Container representing the notification event streams supported by the server
    	**type**\:   :py:class:`Streams <ydk.models.ietf.ietf_restconf_monitoring.RestconfState.Streams>`
    
    

    """

    _prefix = 'rcmon'
    _revision = '2016-08-15'

    def __init__(self):
        super(RestconfState, self).__init__()
        self._top_entity = None

        self.yang_name = "restconf-state"
        self.yang_parent_name = "ietf-restconf-monitoring"

        self.capabilities = RestconfState.Capabilities()
        self.capabilities.parent = self
        self._children_name_map["capabilities"] = "capabilities"
        self._children_yang_names.add("capabilities")

        self.streams = RestconfState.Streams()
        self.streams.parent = self
        self._children_name_map["streams"] = "streams"
        self._children_yang_names.add("streams")


    class Capabilities(Entity):
        """
        Contains a list of protocol capability URIs
        
        .. attribute:: capability
        
        	A RESTCONF protocol capability URI
        	**type**\:  list of str
        
        

        """

        _prefix = 'rcmon'
        _revision = '2016-08-15'

        def __init__(self):
            super(RestconfState.Capabilities, self).__init__()

            self.yang_name = "capabilities"
            self.yang_parent_name = "restconf-state"

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
                        super(RestconfState.Capabilities, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RestconfState.Capabilities, self).__setattr__(name, value)

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
                path_buffer = "ietf-restconf-monitoring:restconf-state/%s" % self.get_segment_path()
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


    class Streams(Entity):
        """
        Container representing the notification event streams
        supported by the server.
        
        .. attribute:: stream
        
        	Each entry describes an event stream supported by the server
        	**type**\: list of    :py:class:`Stream <ydk.models.ietf.ietf_restconf_monitoring.RestconfState.Streams.Stream>`
        
        

        """

        _prefix = 'rcmon'
        _revision = '2016-08-15'

        def __init__(self):
            super(RestconfState.Streams, self).__init__()

            self.yang_name = "streams"
            self.yang_parent_name = "restconf-state"

            self.stream = YList(self)

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
                        super(RestconfState.Streams, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RestconfState.Streams, self).__setattr__(name, value)


        class Stream(Entity):
            """
            Each entry describes an event stream supported by
            the server.
            
            .. attribute:: name  <key>
            
            	The stream name
            	**type**\:  str
            
            .. attribute:: access
            
            	The server will create an entry in this list for each encoding format that is supported for this stream. The media type 'text/event\-stream' is expected for all event streams. This list identifies the sub\-types supported for this stream
            	**type**\: list of    :py:class:`Access <ydk.models.ietf.ietf_restconf_monitoring.RestconfState.Streams.Stream.Access>`
            
            .. attribute:: description
            
            	Description of stream content
            	**type**\:  str
            
            .. attribute:: replay_log_creation_time
            
            	Indicates the time the replay log for this stream was created
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: replay_support
            
            	Indicates if replay buffer supported for this stream. If 'true', then the server MUST support the 'start\-time' and 'stop\-time' query parameters for this stream
            	**type**\:  bool
            
            	**default value**\: false
            
            

            """

            _prefix = 'rcmon'
            _revision = '2016-08-15'

            def __init__(self):
                super(RestconfState.Streams.Stream, self).__init__()

                self.yang_name = "stream"
                self.yang_parent_name = "streams"

                self.name = YLeaf(YType.str, "name")

                self.description = YLeaf(YType.str, "description")

                self.replay_log_creation_time = YLeaf(YType.str, "replay-log-creation-time")

                self.replay_support = YLeaf(YType.boolean, "replay-support")

                self.access = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "description",
                                "replay_log_creation_time",
                                "replay_support") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RestconfState.Streams.Stream, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RestconfState.Streams.Stream, self).__setattr__(name, value)


            class Access(Entity):
                """
                The server will create an entry in this list for each
                encoding format that is supported for this stream.
                The media type 'text/event\-stream' is expected
                for all event streams. This list identifies the
                sub\-types supported for this stream.
                
                .. attribute:: encoding  <key>
                
                	This is the secondary encoding format within the 'text/event\-stream' encoding used by all streams. The type 'xml' is supported for XML encoding.  The type 'json' is supported for JSON encoding
                	**type**\:  str
                
                .. attribute:: location
                
                	Contains a URL that represents the entry point for establishing notification delivery via server sent events
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'rcmon'
                _revision = '2016-08-15'

                def __init__(self):
                    super(RestconfState.Streams.Stream.Access, self).__init__()

                    self.yang_name = "access"
                    self.yang_parent_name = "stream"

                    self.encoding = YLeaf(YType.str, "encoding")

                    self.location = YLeaf(YType.str, "location")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("encoding",
                                    "location") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RestconfState.Streams.Stream.Access, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RestconfState.Streams.Stream.Access, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.encoding.is_set or
                        self.location.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.encoding.yfilter != YFilter.not_set or
                        self.location.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "access" + "[encoding='" + self.encoding.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.encoding.get_name_leafdata())
                    if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.location.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "encoding" or name == "location"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "encoding"):
                        self.encoding = value
                        self.encoding.value_namespace = name_space
                        self.encoding.value_namespace_prefix = name_space_prefix
                    if(value_path == "location"):
                        self.location = value
                        self.location.value_namespace = name_space
                        self.location.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.access:
                    if (c.has_data()):
                        return True
                return (
                    self.name.is_set or
                    self.description.is_set or
                    self.replay_log_creation_time.is_set or
                    self.replay_support.is_set)

            def has_operation(self):
                for c in self.access:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.replay_log_creation_time.yfilter != YFilter.not_set or
                    self.replay_support.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stream" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ietf-restconf-monitoring:restconf-state/streams/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())
                if (self.replay_log_creation_time.is_set or self.replay_log_creation_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.replay_log_creation_time.get_name_leafdata())
                if (self.replay_support.is_set or self.replay_support.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.replay_support.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "access"):
                    for c in self.access:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RestconfState.Streams.Stream.Access()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.access.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access" or name == "name" or name == "description" or name == "replay-log-creation-time" or name == "replay-support"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix
                if(value_path == "replay-log-creation-time"):
                    self.replay_log_creation_time = value
                    self.replay_log_creation_time.value_namespace = name_space
                    self.replay_log_creation_time.value_namespace_prefix = name_space_prefix
                if(value_path == "replay-support"):
                    self.replay_support = value
                    self.replay_support.value_namespace = name_space
                    self.replay_support.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.stream:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.stream:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "streams" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-restconf-monitoring:restconf-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "stream"):
                for c in self.stream:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RestconfState.Streams.Stream()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.stream.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "stream"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.capabilities is not None and self.capabilities.has_data()) or
            (self.streams is not None and self.streams.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.capabilities is not None and self.capabilities.has_operation()) or
            (self.streams is not None and self.streams.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-restconf-monitoring:restconf-state" + path_buffer

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
                self.capabilities = RestconfState.Capabilities()
                self.capabilities.parent = self
                self._children_name_map["capabilities"] = "capabilities"
            return self.capabilities

        if (child_yang_name == "streams"):
            if (self.streams is None):
                self.streams = RestconfState.Streams()
                self.streams.parent = self
                self._children_name_map["streams"] = "streams"
            return self.streams

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "capabilities" or name == "streams"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RestconfState()
        return self._top_entity

