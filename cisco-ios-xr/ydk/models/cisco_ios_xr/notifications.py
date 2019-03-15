""" notifications 

Conversion of the 'ncEvent' XSD in the
NETCONF Notifications RFC.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CreateSubscription(Entity):
    """
    The command to create a notification subscription. It
    takes as argument the name of the notification stream
    and filter. Both of those options limit the content of
    the subscription. In addition, there are two time\-related
    parameters, startTime and stopTime, which can be used to
    select the time interval of interest to the notification
    replay feature.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.notifications.CreateSubscription.Input>`
    
    

    """

    _prefix = 'ncEvent'
    _revision = '2008-07-14'

    def __init__(self):
        super(CreateSubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "create-subscription"
        self.yang_parent_name = "notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CreateSubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._segment_path = lambda: "notifications:create-subscription"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: stream
        
        	An optional parameter that indicates which stream of events is of interest. If not present, then events in the default NETCONF stream will be sent
        	**type**\: str
        
        	**default value**\: NETCONF
        
        .. attribute:: filter
        
        	An optional parameter that indicates which subset of all possible events is of interest. The format of this parameter is the same as that of the filter parameter in the NETCONF protocol operations. If not present, all events not precluded by other parameters will be sent
        	**type**\: anyxml
        
        .. attribute:: starttime
        
        	A parameter used to trigger the replay feature and indicates that the replay should start at the time specified. If start time is not present, this is not a replay subscription
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	An optional parameter used with the optional replay feature to indicate the newest notifications of interest. If stop time is not present, the notifications will continue until the subscription is terminated. Must be used with startTime
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        

        """

        _prefix = 'ncEvent'
        _revision = '2008-07-14'

        def __init__(self):
            super(CreateSubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "create-subscription"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stream', (YLeaf(YType.str, 'stream'), ['str'])),
                ('filter', (YLeaf(YType.str, 'filter'), ['str'])),
                ('starttime', (YLeaf(YType.str, 'startTime'), ['str'])),
                ('stoptime', (YLeaf(YType.str, 'stopTime'), ['str'])),
            ])
            self.stream = None
            self.filter = None
            self.starttime = None
            self.stoptime = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "notifications:create-subscription/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CreateSubscription.Input, [u'stream', u'filter', u'starttime', u'stoptime'], name, value)


    def clone_ptr(self):
        self._top_entity = CreateSubscription()
        return self._top_entity



