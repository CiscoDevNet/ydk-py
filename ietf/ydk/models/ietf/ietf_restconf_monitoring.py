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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class RestconfState(object):
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
        self.capabilities = RestconfState.Capabilities()
        self.capabilities.parent = self
        self.streams = RestconfState.Streams()
        self.streams.parent = self


    class Capabilities(object):
        """
        Contains a list of protocol capability URIs
        
        .. attribute:: capability
        
        	A RESTCONF protocol capability URI
        	**type**\:  list of str
        
        

        """

        _prefix = 'rcmon'
        _revision = '2016-08-15'

        def __init__(self):
            self.parent = None
            self.capability = YLeafList()
            self.capability.parent = self
            self.capability.name = 'capability'

        @property
        def _common_path(self):

            return '/ietf-restconf-monitoring:restconf-state/ietf-restconf-monitoring:capabilities'

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
            from ydk.models.ietf._meta import _ietf_restconf_monitoring as meta
            return meta._meta_table['RestconfState.Capabilities']['meta_info']


    class Streams(object):
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
            self.parent = None
            self.stream = YList()
            self.stream.parent = self
            self.stream.name = 'stream'


        class Stream(object):
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
                self.parent = None
                self.name = None
                self.access = YList()
                self.access.parent = self
                self.access.name = 'access'
                self.description = None
                self.replay_log_creation_time = None
                self.replay_support = None


            class Access(object):
                """
                The server will create an entry in this list for each
                encoding format that is supported for this stream.
                The media type 'text/event\-stream' is expected
                for all event streams. This list identifies the
                sub\-types supported for this stream.
                
                .. attribute:: encoding  <key>
                
                	This is the secondary encoding format within the 'text/event\-stream' encoding used by all streams. The type 'xml' is supported for XML encoding. The type 'json' is supported for JSON encoding
                	**type**\:  str
                
                .. attribute:: location
                
                	Contains a URL that represents the entry point for establishing notification delivery via server sent events
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'rcmon'
                _revision = '2016-08-15'

                def __init__(self):
                    self.parent = None
                    self.encoding = None
                    self.location = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.encoding is None:
                        raise YPYModelError('Key property encoding is None')

                    return self.parent._common_path +'/ietf-restconf-monitoring:access[ietf-restconf-monitoring:encoding = ' + str(self.encoding) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.encoding is not None:
                        return True

                    if self.location is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_restconf_monitoring as meta
                    return meta._meta_table['RestconfState.Streams.Stream.Access']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-restconf-monitoring:restconf-state/ietf-restconf-monitoring:streams/ietf-restconf-monitoring:stream[ietf-restconf-monitoring:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.access is not None:
                    for child_ref in self.access:
                        if child_ref._has_data():
                            return True

                if self.description is not None:
                    return True

                if self.replay_log_creation_time is not None:
                    return True

                if self.replay_support is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_restconf_monitoring as meta
                return meta._meta_table['RestconfState.Streams.Stream']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-restconf-monitoring:restconf-state/ietf-restconf-monitoring:streams'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.stream is not None:
                for child_ref in self.stream:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_restconf_monitoring as meta
            return meta._meta_table['RestconfState.Streams']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-restconf-monitoring:restconf-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.capabilities is not None and self.capabilities._has_data():
            return True

        if self.streams is not None and self.streams._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_restconf_monitoring as meta
        return meta._meta_table['RestconfState']['meta_info']


