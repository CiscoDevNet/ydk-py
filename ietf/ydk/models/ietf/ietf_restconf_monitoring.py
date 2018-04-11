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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RestconfState(Entity):
    """
    Contains RESTCONF protocol monitoring information.
    
    .. attribute:: capabilities
    
    	Contains a list of protocol capability URIs
    	**type**\:  :py:class:`Capabilities <ydk.models.ietf.ietf_restconf_monitoring.RestconfState.Capabilities>`
    
    .. attribute:: streams
    
    	Container representing the notification event streams supported by the server
    	**type**\:  :py:class:`Streams <ydk.models.ietf.ietf_restconf_monitoring.RestconfState.Streams>`
    
    

    """

    _prefix = 'rcmon'
    _revision = '2016-08-15'

    def __init__(self):
        super(RestconfState, self).__init__()
        self._top_entity = None

        self.yang_name = "restconf-state"
        self.yang_parent_name = "ietf-restconf-monitoring"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("capabilities", ("capabilities", RestconfState.Capabilities)), ("streams", ("streams", RestconfState.Streams))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.capabilities = RestconfState.Capabilities()
        self.capabilities.parent = self
        self._children_name_map["capabilities"] = "capabilities"
        self._children_yang_names.add("capabilities")

        self.streams = RestconfState.Streams()
        self.streams.parent = self
        self._children_name_map["streams"] = "streams"
        self._children_yang_names.add("streams")
        self._segment_path = lambda: "ietf-restconf-monitoring:restconf-state"


    class Capabilities(Entity):
        """
        Contains a list of protocol capability URIs
        
        .. attribute:: capability
        
        	A RESTCONF protocol capability URI
        	**type**\: list of str
        
        

        """

        _prefix = 'rcmon'
        _revision = '2016-08-15'

        def __init__(self):
            super(RestconfState.Capabilities, self).__init__()

            self.yang_name = "capabilities"
            self.yang_parent_name = "restconf-state"
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
            self._absolute_path = lambda: "ietf-restconf-monitoring:restconf-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RestconfState.Capabilities, ['capability'], name, value)


    class Streams(Entity):
        """
        Container representing the notification event streams
        supported by the server.
        
        .. attribute:: stream
        
        	Each entry describes an event stream supported by the server
        	**type**\: list of  		 :py:class:`Stream <ydk.models.ietf.ietf_restconf_monitoring.RestconfState.Streams.Stream>`
        
        

        """

        _prefix = 'rcmon'
        _revision = '2016-08-15'

        def __init__(self):
            super(RestconfState.Streams, self).__init__()

            self.yang_name = "streams"
            self.yang_parent_name = "restconf-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("stream", ("stream", RestconfState.Streams.Stream))])
            self._leafs = OrderedDict()

            self.stream = YList(self)
            self._segment_path = lambda: "streams"
            self._absolute_path = lambda: "ietf-restconf-monitoring:restconf-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RestconfState.Streams, [], name, value)


        class Stream(Entity):
            """
            Each entry describes an event stream supported by
            the server.
            
            .. attribute:: name  (key)
            
            	The stream name
            	**type**\: str
            
            .. attribute:: description
            
            	Description of stream content
            	**type**\: str
            
            .. attribute:: replay_support
            
            	Indicates if replay buffer supported for this stream. If 'true', then the server MUST support the 'start\-time' and 'stop\-time' query parameters for this stream
            	**type**\: bool
            
            	**default value**\: false
            
            .. attribute:: replay_log_creation_time
            
            	Indicates the time the replay log for this stream was created
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: access
            
            	The server will create an entry in this list for each encoding format that is supported for this stream. The media type 'text/event\-stream' is expected for all event streams. This list identifies the sub\-types supported for this stream
            	**type**\: list of  		 :py:class:`Access <ydk.models.ietf.ietf_restconf_monitoring.RestconfState.Streams.Stream.Access>`
            
            

            """

            _prefix = 'rcmon'
            _revision = '2016-08-15'

            def __init__(self):
                super(RestconfState.Streams.Stream, self).__init__()

                self.yang_name = "stream"
                self.yang_parent_name = "streams"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("access", ("access", RestconfState.Streams.Stream.Access))])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('description', YLeaf(YType.str, 'description')),
                    ('replay_support', YLeaf(YType.boolean, 'replay-support')),
                    ('replay_log_creation_time', YLeaf(YType.str, 'replay-log-creation-time')),
                ])
                self.name = None
                self.description = None
                self.replay_support = None
                self.replay_log_creation_time = None

                self.access = YList(self)
                self._segment_path = lambda: "stream" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "ietf-restconf-monitoring:restconf-state/streams/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RestconfState.Streams.Stream, ['name', 'description', 'replay_support', 'replay_log_creation_time'], name, value)


            class Access(Entity):
                """
                The server will create an entry in this list for each
                encoding format that is supported for this stream.
                The media type 'text/event\-stream' is expected
                for all event streams. This list identifies the
                sub\-types supported for this stream.
                
                .. attribute:: encoding  (key)
                
                	This is the secondary encoding format within the 'text/event\-stream' encoding used by all streams. The type 'xml' is supported for XML encoding. The type 'json' is supported for JSON encoding
                	**type**\: str
                
                .. attribute:: location
                
                	Contains a URL that represents the entry point for establishing notification delivery via server sent events
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'rcmon'
                _revision = '2016-08-15'

                def __init__(self):
                    super(RestconfState.Streams.Stream.Access, self).__init__()

                    self.yang_name = "access"
                    self.yang_parent_name = "stream"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['encoding']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('encoding', YLeaf(YType.str, 'encoding')),
                        ('location', YLeaf(YType.str, 'location')),
                    ])
                    self.encoding = None
                    self.location = None
                    self._segment_path = lambda: "access" + "[encoding='" + str(self.encoding) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(RestconfState.Streams.Stream.Access, ['encoding', 'location'], name, value)

    def clone_ptr(self):
        self._top_entity = RestconfState()
        return self._top_entity

