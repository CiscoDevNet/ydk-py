""" nc_notifications 

Conversion of the 'manageEvent' XSD in the NETCONF
Notifications RFC.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Netconf(_Entity_):
    """
    Top\-level element in the notification namespace
    
    .. attribute:: streams
    
    	The list of event streams supported by the system. When a query is issued, the returned set of streams is  determined based on user privileges
    	**type**\:  :py:class:`Streams <ydk.models.cisco_ios_xr.nc_notifications.Netconf.Streams>`
    
    	**config**\: False
    
    

    """

    _prefix = 'manageEvent'
    _revision = '2008-07-14'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Netconf, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf"
        self.yang_parent_name = "nc-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("streams", ("streams", Netconf.Streams))])
        self._leafs = OrderedDict()

        self.streams = Netconf.Streams()
        self.streams.parent = self
        self._children_name_map["streams"] = "streams"
        self._segment_path = lambda: "nc-notifications:netconf"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Netconf, [], name, value)


    class Streams(_Entity_):
        """
        The list of event streams supported by the system. When
        a query is issued, the returned set of streams is 
        determined based on user privileges.
        
        .. attribute:: stream
        
        	Stream name, description and other information
        	**type**\: list of  		 :py:class:`Stream <ydk.models.cisco_ios_xr.nc_notifications.Netconf.Streams.Stream>`
        
        	**config**\: False
        
        

        """

        _prefix = 'manageEvent'
        _revision = '2008-07-14'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Netconf.Streams, self).__init__()

            self.yang_name = "streams"
            self.yang_parent_name = "netconf"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("stream", ("stream", Netconf.Streams.Stream))])
            self._leafs = OrderedDict()

            self.stream = YList(self)
            self._segment_path = lambda: "streams"
            self._absolute_path = lambda: "nc-notifications:netconf/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Netconf.Streams, [], name, value)


        class Stream(_Entity_):
            """
            Stream name, description and other information.
            
            .. attribute:: name  (key)
            
            	The name of the event stream. If this is the default NETCONF stream, this must have the value 'NETCONF'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: description
            
            	A description of the event stream, including such information as the type of events that are sent over this stream
            	**type**\: str
            
            	**mandatory**\: True
            
            	**config**\: False
            
            .. attribute:: replaysupport
            
            	A description of the event stream, including such information as the type of events that are sent over this stream
            	**type**\: bool
            
            	**mandatory**\: True
            
            	**config**\: False
            
            .. attribute:: replaylogcreationtime
            
            	The timestamp of the creation of the log used to support the replay function on this stream. Note that this might be earlier then the earliest available notification in the log. This object is updated if the log resets for  some reason.  This object MUST be present if replay is supported
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**config**\: False
            
            

            """

            _prefix = 'manageEvent'
            _revision = '2008-07-14'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Netconf.Streams.Stream, self).__init__()

                self.yang_name = "stream"
                self.yang_parent_name = "streams"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('replaysupport', (YLeaf(YType.boolean, 'replaySupport'), ['bool'])),
                    ('replaylogcreationtime', (YLeaf(YType.str, 'replayLogCreationTime'), ['str'])),
                ])
                self.name = None
                self.description = None
                self.replaysupport = None
                self.replaylogcreationtime = None
                self._segment_path = lambda: "stream" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "nc-notifications:netconf/streams/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Netconf.Streams.Stream, ['name', 'description', 'replaysupport', 'replaylogcreationtime'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _nc_notifications as meta
                return meta._meta_table['Netconf.Streams.Stream']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _nc_notifications as meta
            return meta._meta_table['Netconf.Streams']['meta_info']

    def clone_ptr(self):
        self._top_entity = Netconf()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _nc_notifications as meta
        return meta._meta_table['Netconf']['meta_info']


