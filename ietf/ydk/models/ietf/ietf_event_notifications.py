""" ietf_event_notifications 

This module contains conceptual YANG specifications
for NETCONF Event Notifications.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PushSource(Enum):
    """
    PushSource (Enum Class)

    Specifies from where notifications will be sourced when

    being sent by the publisher.

    .. data:: interface_originated = 0

    	Notifications will be sent from a specific interface on

    	a publisher

    .. data:: address_originated = 1

    	Notifications will be sent from a specific address on a

    	publisher

    """

    interface_originated = Enum.YLeaf(0, "interface-originated")

    address_originated = Enum.YLeaf(1, "address-originated")



class Stream(Identity):
    """
    Base identity to represent a generic stream of event
    notifications.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Stream, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:stream")


class SubscriptionResult(Identity):
    """
    Base identity for RPC responses to requests surrounding
    management (e.g. creation, modification, deletion) of
    subscriptions.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(SubscriptionResult, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:subscription-result")


class SubscriptionStreamStatus(Identity):
    """
    Base identity for the status of subscriptions and
    datastreams.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(SubscriptionStreamStatus, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:subscription-stream-status")


class SubscriptionErrors(Identity):
    """
    Base identity for subscription error status.
    This identity is not to be confused with error return
    codes for RPCs
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(SubscriptionErrors, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:subscription-errors")


class Encodings(Identity):
    """
    Base identity to represent data encodings
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Encodings, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:encodings")


class Transport(Identity):
    """
    An identity that represents a transport protocol for
    event notifications
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Transport, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:transport")


class EstablishSubscription(Entity):
    """
    This RPC allows a subscriber to create
    (and possibly negotiate) a subscription on its own behalf.
    If successful, the subscription
    remains in effect for the duration of the subscriber's
    association with the publisher, or until the subscription
    is terminated by virtue of a delete\-subscription request.
    In case an error (as indicated by subscription\-result)
    is returned, the subscription is
    not created.  In that case, the RPC output
    MAY include suggested parameter settings
    that would have a high likelihood of succeeding in a
    subsequent establish\-subscription request.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.ietf.ietf_event_notifications.EstablishSubscription.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.ietf.ietf_event_notifications.EstablishSubscription.Output>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(EstablishSubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "establish-subscription"
        self.yang_parent_name = "ietf-event-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = EstablishSubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = EstablishSubscription.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "ietf-event-notifications:establish-subscription"


    class Input(Entity):
        """
        
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:  :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:  :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\: anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\: anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\: str
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\: list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\: int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\: str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(EstablishSubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "establish-subscription"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stream', YLeaf(YType.identityref, 'stream')),
                ('encoding', YLeaf(YType.identityref, 'encoding')),
                ('filter', YLeaf(YType.str, 'filter')),
                ('filter_ref', YLeaf(YType.str, 'filter-ref')),
                ('subtree_filter', YLeaf(YType.str, 'ietf-yang-push:subtree-filter')),
                ('xpath_filter', YLeaf(YType.str, 'ietf-yang-push:xpath-filter')),
                ('starttime', YLeaf(YType.str, 'startTime')),
                ('stoptime', YLeaf(YType.str, 'stopTime')),
                ('period', YLeaf(YType.uint32, 'ietf-yang-push:period')),
                ('anchor_time', YLeaf(YType.str, 'ietf-yang-push:anchor-time')),
                ('no_synch_on_start', YLeaf(YType.empty, 'ietf-yang-push:no-synch-on-start')),
                ('dampening_period', YLeaf(YType.uint32, 'ietf-yang-push:dampening-period')),
                ('excluded_change', YLeafList(YType.enumeration, 'ietf-yang-push:excluded-change')),
                ('dscp', YLeaf(YType.uint8, 'ietf-yang-push:dscp')),
                ('subscription_priority', YLeaf(YType.uint8, 'ietf-yang-push:subscription-priority')),
                ('subscription_dependency', YLeaf(YType.str, 'ietf-yang-push:subscription-dependency')),
            ])
            self.stream = None
            self.encoding = None
            self.filter = None
            self.filter_ref = None
            self.subtree_filter = None
            self.xpath_filter = None
            self.starttime = None
            self.stoptime = None
            self.period = None
            self.anchor_time = None
            self.no_synch_on_start = None
            self.dampening_period = None
            self.excluded_change = []
            self.dscp = None
            self.subscription_priority = None
            self.subscription_dependency = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "ietf-event-notifications:establish-subscription/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EstablishSubscription.Input, ['stream', 'encoding', 'filter', 'filter_ref', 'subtree_filter', 'xpath_filter', 'starttime', 'stoptime', 'period', 'anchor_time', 'no_synch_on_start', 'dampening_period', 'excluded_change', 'dscp', 'subscription_priority', 'subscription_dependency'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:  :py:class:`SubscriptionResult <ydk.models.ietf.ietf_event_notifications.SubscriptionResult>`
        
        	**mandatory**\: True
        
        .. attribute:: subscription_id
        
        	Identifier used for this subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:  :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:  :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\: anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\: anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\: str
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\: list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\: int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\: str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(EstablishSubscription.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "establish-subscription"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('subscription_result', YLeaf(YType.identityref, 'subscription-result')),
                ('subscription_id', YLeaf(YType.uint32, 'subscription-id')),
                ('stream', YLeaf(YType.identityref, 'stream')),
                ('encoding', YLeaf(YType.identityref, 'encoding')),
                ('filter', YLeaf(YType.str, 'filter')),
                ('filter_ref', YLeaf(YType.str, 'filter-ref')),
                ('subtree_filter', YLeaf(YType.str, 'ietf-yang-push:subtree-filter')),
                ('xpath_filter', YLeaf(YType.str, 'ietf-yang-push:xpath-filter')),
                ('starttime', YLeaf(YType.str, 'startTime')),
                ('stoptime', YLeaf(YType.str, 'stopTime')),
                ('period', YLeaf(YType.uint32, 'ietf-yang-push:period')),
                ('anchor_time', YLeaf(YType.str, 'ietf-yang-push:anchor-time')),
                ('no_synch_on_start', YLeaf(YType.empty, 'ietf-yang-push:no-synch-on-start')),
                ('dampening_period', YLeaf(YType.uint32, 'ietf-yang-push:dampening-period')),
                ('excluded_change', YLeafList(YType.enumeration, 'ietf-yang-push:excluded-change')),
                ('dscp', YLeaf(YType.uint8, 'ietf-yang-push:dscp')),
                ('subscription_priority', YLeaf(YType.uint8, 'ietf-yang-push:subscription-priority')),
                ('subscription_dependency', YLeaf(YType.str, 'ietf-yang-push:subscription-dependency')),
            ])
            self.subscription_result = None
            self.subscription_id = None
            self.stream = None
            self.encoding = None
            self.filter = None
            self.filter_ref = None
            self.subtree_filter = None
            self.xpath_filter = None
            self.starttime = None
            self.stoptime = None
            self.period = None
            self.anchor_time = None
            self.no_synch_on_start = None
            self.dampening_period = None
            self.excluded_change = []
            self.dscp = None
            self.subscription_priority = None
            self.subscription_dependency = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "ietf-event-notifications:establish-subscription/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EstablishSubscription.Output, ['subscription_result', 'subscription_id', 'stream', 'encoding', 'filter', 'filter_ref', 'subtree_filter', 'xpath_filter', 'starttime', 'stoptime', 'period', 'anchor_time', 'no_synch_on_start', 'dampening_period', 'excluded_change', 'dscp', 'subscription_priority', 'subscription_dependency'], name, value)

    def clone_ptr(self):
        self._top_entity = EstablishSubscription()
        return self._top_entity

class CreateSubscription(Entity):
    """
    This operation initiates an event notification subscription
    that will send asynchronous event notifications to the
    initiator of the command until the association terminates.
    It is not possible to modify or delete a subscription
    that was created using this operation.  It is included for
    reasons of backward compatibility with RFC 5277
    implementations.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.ietf.ietf_event_notifications.CreateSubscription.Input>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(CreateSubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "create-subscription"
        self.yang_parent_name = "ietf-event-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CreateSubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "ietf-event-notifications:create-subscription"


    class Input(Entity):
        """
        
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:  :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        	**default value**\: NETCONF
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:  :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\: anyxml
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(CreateSubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "create-subscription"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('stream', YLeaf(YType.identityref, 'stream')),
                ('encoding', YLeaf(YType.identityref, 'encoding')),
                ('filter', YLeaf(YType.str, 'filter')),
                ('starttime', YLeaf(YType.str, 'startTime')),
                ('stoptime', YLeaf(YType.str, 'stopTime')),
            ])
            self.stream = None
            self.encoding = None
            self.filter = None
            self.starttime = None
            self.stoptime = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "ietf-event-notifications:create-subscription/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CreateSubscription.Input, ['stream', 'encoding', 'filter', 'starttime', 'stoptime'], name, value)

    def clone_ptr(self):
        self._top_entity = CreateSubscription()
        return self._top_entity

class ModifySubscription(Entity):
    """
    This RPC allows a subscriber to modify a subscription
    that was previously created using establish\-subscription.
    If successful, the subscription
    remains in effect for the duration of the subscriber's
    association with the publisher, or until the subscription
    is terminated by virtue of a delete\-subscription request.
    In case an error is returned (as indicated by
    subscription\-result), the subscription is
    not modified and the original subscription parameters
    remain in effect.  In that case, the rpc error response
    MAY include suggested parameter settings
    that would have a high likelihood of succeeding in a
    subsequent modify\-subscription request.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.ietf.ietf_event_notifications.ModifySubscription.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.ietf.ietf_event_notifications.ModifySubscription.Output>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ModifySubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "modify-subscription"
        self.yang_parent_name = "ietf-event-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ModifySubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = ModifySubscription.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "ietf-event-notifications:modify-subscription"


    class Input(Entity):
        """
        
        
        .. attribute:: subscription_id
        
        	Identifier to use for this subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\: anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\: anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\: str
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\: list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(ModifySubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "modify-subscription"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('subscription_id', YLeaf(YType.uint32, 'subscription-id')),
                ('filter', YLeaf(YType.str, 'filter')),
                ('filter_ref', YLeaf(YType.str, 'filter-ref')),
                ('subtree_filter', YLeaf(YType.str, 'ietf-yang-push:subtree-filter')),
                ('xpath_filter', YLeaf(YType.str, 'ietf-yang-push:xpath-filter')),
                ('starttime', YLeaf(YType.str, 'startTime')),
                ('stoptime', YLeaf(YType.str, 'stopTime')),
                ('period', YLeaf(YType.uint32, 'ietf-yang-push:period')),
                ('anchor_time', YLeaf(YType.str, 'ietf-yang-push:anchor-time')),
                ('no_synch_on_start', YLeaf(YType.empty, 'ietf-yang-push:no-synch-on-start')),
                ('dampening_period', YLeaf(YType.uint32, 'ietf-yang-push:dampening-period')),
                ('excluded_change', YLeafList(YType.enumeration, 'ietf-yang-push:excluded-change')),
            ])
            self.subscription_id = None
            self.filter = None
            self.filter_ref = None
            self.subtree_filter = None
            self.xpath_filter = None
            self.starttime = None
            self.stoptime = None
            self.period = None
            self.anchor_time = None
            self.no_synch_on_start = None
            self.dampening_period = None
            self.excluded_change = []
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "ietf-event-notifications:modify-subscription/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ModifySubscription.Input, ['subscription_id', 'filter', 'filter_ref', 'subtree_filter', 'xpath_filter', 'starttime', 'stoptime', 'period', 'anchor_time', 'no_synch_on_start', 'dampening_period', 'excluded_change'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:  :py:class:`SubscriptionResult <ydk.models.ietf.ietf_event_notifications.SubscriptionResult>`
        
        	**mandatory**\: True
        
        .. attribute:: subscription_id
        
        	Identifier used for this subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:  :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:  :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\: anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\: anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\: str
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\: list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\: int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\: str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(ModifySubscription.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "modify-subscription"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('subscription_result', YLeaf(YType.identityref, 'subscription-result')),
                ('subscription_id', YLeaf(YType.uint32, 'subscription-id')),
                ('stream', YLeaf(YType.identityref, 'stream')),
                ('encoding', YLeaf(YType.identityref, 'encoding')),
                ('filter', YLeaf(YType.str, 'filter')),
                ('filter_ref', YLeaf(YType.str, 'filter-ref')),
                ('subtree_filter', YLeaf(YType.str, 'ietf-yang-push:subtree-filter')),
                ('xpath_filter', YLeaf(YType.str, 'ietf-yang-push:xpath-filter')),
                ('starttime', YLeaf(YType.str, 'startTime')),
                ('stoptime', YLeaf(YType.str, 'stopTime')),
                ('period', YLeaf(YType.uint32, 'ietf-yang-push:period')),
                ('anchor_time', YLeaf(YType.str, 'ietf-yang-push:anchor-time')),
                ('no_synch_on_start', YLeaf(YType.empty, 'ietf-yang-push:no-synch-on-start')),
                ('dampening_period', YLeaf(YType.uint32, 'ietf-yang-push:dampening-period')),
                ('excluded_change', YLeafList(YType.enumeration, 'ietf-yang-push:excluded-change')),
                ('dscp', YLeaf(YType.uint8, 'ietf-yang-push:dscp')),
                ('subscription_priority', YLeaf(YType.uint8, 'ietf-yang-push:subscription-priority')),
                ('subscription_dependency', YLeaf(YType.str, 'ietf-yang-push:subscription-dependency')),
            ])
            self.subscription_result = None
            self.subscription_id = None
            self.stream = None
            self.encoding = None
            self.filter = None
            self.filter_ref = None
            self.subtree_filter = None
            self.xpath_filter = None
            self.starttime = None
            self.stoptime = None
            self.period = None
            self.anchor_time = None
            self.no_synch_on_start = None
            self.dampening_period = None
            self.excluded_change = []
            self.dscp = None
            self.subscription_priority = None
            self.subscription_dependency = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "ietf-event-notifications:modify-subscription/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ModifySubscription.Output, ['subscription_result', 'subscription_id', 'stream', 'encoding', 'filter', 'filter_ref', 'subtree_filter', 'xpath_filter', 'starttime', 'stoptime', 'period', 'anchor_time', 'no_synch_on_start', 'dampening_period', 'excluded_change', 'dscp', 'subscription_priority', 'subscription_dependency'], name, value)

    def clone_ptr(self):
        self._top_entity = ModifySubscription()
        return self._top_entity

class DeleteSubscription(Entity):
    """
    This RPC allows a subscriber to delete a subscription that
    was previously created using establish\-subscription.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.ietf.ietf_event_notifications.DeleteSubscription.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.ietf.ietf_event_notifications.DeleteSubscription.Output>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(DeleteSubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "delete-subscription"
        self.yang_parent_name = "ietf-event-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = DeleteSubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = DeleteSubscription.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "ietf-event-notifications:delete-subscription"


    class Input(Entity):
        """
        
        
        .. attribute:: subscription_id
        
        	Identifier of the subscription that is to be deleted. Only subscriptions that were created using establish\-subscription can be deleted via this RPC
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(DeleteSubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "delete-subscription"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('subscription_id', YLeaf(YType.uint32, 'subscription-id')),
            ])
            self.subscription_id = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "ietf-event-notifications:delete-subscription/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DeleteSubscription.Input, ['subscription_id'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:  :py:class:`SubscriptionResult <ydk.models.ietf.ietf_event_notifications.SubscriptionResult>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(DeleteSubscription.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "delete-subscription"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('subscription_result', YLeaf(YType.identityref, 'subscription-result')),
            ])
            self.subscription_result = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "ietf-event-notifications:delete-subscription/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DeleteSubscription.Output, ['subscription_result'], name, value)

    def clone_ptr(self):
        self._top_entity = DeleteSubscription()
        return self._top_entity

class Streams(Entity):
    """
    This container contains a leaf list of built\-in
    streams that are provided by the system.
    
    .. attribute:: stream
    
    	Identifies the built\-in streams that are supported by the system.  Built\-in streams are associated with their own identities, each of which carries a special semantics. In case configurable custom streams are supported, as indicated by the custom\-stream identity, the configuration of those custom streams is provided         separately
    	**type**\: list of   :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Streams, self).__init__()
        self._top_entity = None

        self.yang_name = "streams"
        self.yang_parent_name = "ietf-event-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('stream', YLeafList(YType.identityref, 'stream')),
        ])
        self.stream = []
        self._segment_path = lambda: "ietf-event-notifications:streams"

    def __setattr__(self, name, value):
        self._perform_setattr(Streams, ['stream'], name, value)

    def clone_ptr(self):
        self._top_entity = Streams()
        return self._top_entity

class Filters(Entity):
    """
    This container contains a list of configurable filters
    that can be applied to subscriptions.  This facilitates
    the reuse of complex filters once defined.
    
    .. attribute:: filter
    
    	A list of configurable filters that can be applied to subscriptions
    	**type**\: list of  		 :py:class:`Filter <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Filters, self).__init__()
        self._top_entity = None

        self.yang_name = "filters"
        self.yang_parent_name = "ietf-event-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("filter", ("filter", Filters.Filter))])
        self._leafs = OrderedDict()

        self.filter = YList(self)
        self._segment_path = lambda: "ietf-event-notifications:filters"

    def __setattr__(self, name, value):
        self._perform_setattr(Filters, [], name, value)


    class Filter(Entity):
        """
        A list of configurable filters that can be applied to
        subscriptions.
        
        .. attribute:: filter_id  (key)
        
        	An identifier to differentiate between filters
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\: anyxml
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\: anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\: str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(Filters.Filter, self).__init__()

            self.yang_name = "filter"
            self.yang_parent_name = "filters"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['filter_id']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('filter_id', YLeaf(YType.uint32, 'filter-id')),
                ('filter', YLeaf(YType.str, 'filter')),
                ('subtree_filter', YLeaf(YType.str, 'ietf-yang-push:subtree-filter')),
                ('xpath_filter', YLeaf(YType.str, 'ietf-yang-push:xpath-filter')),
            ])
            self.filter_id = None
            self.filter = None
            self.subtree_filter = None
            self.xpath_filter = None
            self._segment_path = lambda: "filter" + "[filter-id='" + str(self.filter_id) + "']"
            self._absolute_path = lambda: "ietf-event-notifications:filters/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Filters.Filter, ['filter_id', 'filter', 'subtree_filter', 'xpath_filter'], name, value)

    def clone_ptr(self):
        self._top_entity = Filters()
        return self._top_entity

class SubscriptionConfig(Entity):
    """
    Contains the list of subscriptions that are configured,
    as opposed to established via RPC or other means.
    
    .. attribute:: subscription
    
    	Content of a subscription
    	**type**\: list of  		 :py:class:`Subscription <ydk.models.ietf.ietf_event_notifications.SubscriptionConfig.Subscription>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(SubscriptionConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "subscription-config"
        self.yang_parent_name = "ietf-event-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("subscription", ("subscription", SubscriptionConfig.Subscription))])
        self._leafs = OrderedDict()

        self.subscription = YList(self)
        self._segment_path = lambda: "ietf-event-notifications:subscription-config"

    def __setattr__(self, name, value):
        self._perform_setattr(SubscriptionConfig, [], name, value)


    class Subscription(Entity):
        """
        Content of a subscription.
        
        .. attribute:: subscription_id  (key)
        
        	Identifier to use for this subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:  :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:  :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\: anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\: anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\: str
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: receivers
        
        	Set of receivers in a subscription
        	**type**\:  :py:class:`Receivers <ydk.models.ietf.ietf_event_notifications.SubscriptionConfig.Subscription.Receivers>`
        
        .. attribute:: source_interface
        
        	References the interface for notifications
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        .. attribute:: source_vrf
        
        	Label of the vrf
        	**type**\: int
        
        	**range:** 16..1048574
        
        .. attribute:: source_address
        
        	The source address for the notifications
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\: list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\: int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\: str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(SubscriptionConfig.Subscription, self).__init__()

            self.yang_name = "subscription"
            self.yang_parent_name = "subscription-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['subscription_id']
            self._child_container_classes = OrderedDict([("receivers", ("receivers", SubscriptionConfig.Subscription.Receivers))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('subscription_id', YLeaf(YType.uint32, 'subscription-id')),
                ('stream', YLeaf(YType.identityref, 'stream')),
                ('encoding', YLeaf(YType.identityref, 'encoding')),
                ('filter', YLeaf(YType.str, 'filter')),
                ('filter_ref', YLeaf(YType.str, 'filter-ref')),
                ('subtree_filter', YLeaf(YType.str, 'ietf-yang-push:subtree-filter')),
                ('xpath_filter', YLeaf(YType.str, 'ietf-yang-push:xpath-filter')),
                ('starttime', YLeaf(YType.str, 'startTime')),
                ('stoptime', YLeaf(YType.str, 'stopTime')),
                ('source_interface', YLeaf(YType.str, 'source-interface')),
                ('source_vrf', YLeaf(YType.uint32, 'source-vrf')),
                ('source_address', YLeaf(YType.str, 'source-address')),
                ('period', YLeaf(YType.uint32, 'ietf-yang-push:period')),
                ('anchor_time', YLeaf(YType.str, 'ietf-yang-push:anchor-time')),
                ('no_synch_on_start', YLeaf(YType.empty, 'ietf-yang-push:no-synch-on-start')),
                ('dampening_period', YLeaf(YType.uint32, 'ietf-yang-push:dampening-period')),
                ('excluded_change', YLeafList(YType.enumeration, 'ietf-yang-push:excluded-change')),
                ('dscp', YLeaf(YType.uint8, 'ietf-yang-push:dscp')),
                ('subscription_priority', YLeaf(YType.uint8, 'ietf-yang-push:subscription-priority')),
                ('subscription_dependency', YLeaf(YType.str, 'ietf-yang-push:subscription-dependency')),
            ])
            self.subscription_id = None
            self.stream = None
            self.encoding = None
            self.filter = None
            self.filter_ref = None
            self.subtree_filter = None
            self.xpath_filter = None
            self.starttime = None
            self.stoptime = None
            self.source_interface = None
            self.source_vrf = None
            self.source_address = None
            self.period = None
            self.anchor_time = None
            self.no_synch_on_start = None
            self.dampening_period = None
            self.excluded_change = []
            self.dscp = None
            self.subscription_priority = None
            self.subscription_dependency = None

            self.receivers = SubscriptionConfig.Subscription.Receivers()
            self.receivers.parent = self
            self._children_name_map["receivers"] = "receivers"
            self._children_yang_names.add("receivers")
            self._segment_path = lambda: "subscription" + "[subscription-id='" + str(self.subscription_id) + "']"
            self._absolute_path = lambda: "ietf-event-notifications:subscription-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriptionConfig.Subscription, ['subscription_id', 'stream', 'encoding', 'filter', 'filter_ref', 'subtree_filter', 'xpath_filter', 'starttime', 'stoptime', 'source_interface', 'source_vrf', 'source_address', 'period', 'anchor_time', 'no_synch_on_start', 'dampening_period', 'excluded_change', 'dscp', 'subscription_priority', 'subscription_dependency'], name, value)


        class Receivers(Entity):
            """
            Set of receivers in a subscription.
            
            .. attribute:: receiver
            
            	A single host or multipoint address intended as a target for the notifications for a subscription
            	**type**\: list of  		 :py:class:`Receiver <ydk.models.ietf.ietf_event_notifications.SubscriptionConfig.Subscription.Receivers.Receiver>`
            
            

            """

            _prefix = 'notif-bis'
            _revision = '2016-10-27'

            def __init__(self):
                super(SubscriptionConfig.Subscription.Receivers, self).__init__()

                self.yang_name = "receivers"
                self.yang_parent_name = "subscription"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("receiver", ("receiver", SubscriptionConfig.Subscription.Receivers.Receiver))])
                self._leafs = OrderedDict()

                self.receiver = YList(self)
                self._segment_path = lambda: "receivers"

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriptionConfig.Subscription.Receivers, [], name, value)


            class Receiver(Entity):
                """
                A single host or multipoint address intended as a target
                for the notifications for a subscription.
                
                .. attribute:: address  (key)
                
                	Specifies the address for the traffic to reach a remote host. One of the following must be specified\: an ipv4 address, an ipv6 address, or a host name
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
                
                	**mandatory**\: True
                
                .. attribute:: port
                
                	This leaf specifies the port number to use for messages destined for a receiver
                	**type**\: int
                
                	**range:** 0..65535
                
                	**mandatory**\: True
                
                .. attribute:: protocol
                
                	This leaf specifies the transport protocol used to deliver messages destined for the receiver
                	**type**\:  :py:class:`Transport <ydk.models.ietf.ietf_event_notifications.Transport>`
                
                	**default value**\: netconf
                
                

                """

                _prefix = 'notif-bis'
                _revision = '2016-10-27'

                def __init__(self):
                    super(SubscriptionConfig.Subscription.Receivers.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "receivers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['address']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address', YLeaf(YType.str, 'address')),
                        ('port', YLeaf(YType.uint16, 'port')),
                        ('protocol', YLeaf(YType.identityref, 'protocol')),
                    ])
                    self.address = None
                    self.port = None
                    self.protocol = None
                    self._segment_path = lambda: "receiver" + "[address='" + str(self.address) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriptionConfig.Subscription.Receivers.Receiver, ['address', 'port', 'protocol'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriptionConfig()
        return self._top_entity

class Subscriptions(Entity):
    """
    Contains the list of currently active subscriptions,
    i.e. subscriptions that are currently in effect,
    used for subscription management and monitoring purposes.
    This includes subscriptions that have been setup via RPC
    primitives, e.g. create\-subscription, establish\-
    subscription, and modify\-subscription, as well as
    subscriptions that have been established via
        configuration.
    
    .. attribute:: subscription
    
    	Content of a subscription. Subscriptions can be created using a control channel or RPC, or be established through configuration
    	**type**\: list of  		 :py:class:`Subscription <ydk.models.ietf.ietf_event_notifications.Subscriptions.Subscription>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Subscriptions, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriptions"
        self.yang_parent_name = "ietf-event-notifications"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("subscription", ("subscription", Subscriptions.Subscription))])
        self._leafs = OrderedDict()

        self.subscription = YList(self)
        self._segment_path = lambda: "ietf-event-notifications:subscriptions"

    def __setattr__(self, name, value):
        self._perform_setattr(Subscriptions, [], name, value)


    class Subscription(Entity):
        """
        Content of a subscription.
        Subscriptions can be created using a control channel
        or RPC, or be established through configuration.
        
        .. attribute:: subscription_id  (key)
        
        	Identifier of this subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: configured_subscription
        
        	The presence of this leaf indicates that the subscription originated from configuration, not through a control channel or RPC
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: subscription_status
        
        	The status of the subscription
        	**type**\:  :py:class:`SubscriptionStreamStatus <ydk.models.ietf.ietf_event_notifications.SubscriptionStreamStatus>`
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:  :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:  :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\: anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\: anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\: str
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: receivers
        
        	Set of receivers in a subscription
        	**type**\:  :py:class:`Receivers <ydk.models.ietf.ietf_event_notifications.Subscriptions.Subscription.Receivers>`
        
        .. attribute:: source_interface
        
        	References the interface for notifications
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        .. attribute:: source_vrf
        
        	Label of the vrf
        	**type**\: int
        
        	**range:** 16..1048574
        
        .. attribute:: source_address
        
        	The source address for the notifications
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\: list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\: int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\: str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(Subscriptions.Subscription, self).__init__()

            self.yang_name = "subscription"
            self.yang_parent_name = "subscriptions"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['subscription_id']
            self._child_container_classes = OrderedDict([("receivers", ("receivers", Subscriptions.Subscription.Receivers))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('subscription_id', YLeaf(YType.uint32, 'subscription-id')),
                ('configured_subscription', YLeaf(YType.empty, 'configured-subscription')),
                ('subscription_status', YLeaf(YType.identityref, 'subscription-status')),
                ('stream', YLeaf(YType.identityref, 'stream')),
                ('encoding', YLeaf(YType.identityref, 'encoding')),
                ('filter', YLeaf(YType.str, 'filter')),
                ('filter_ref', YLeaf(YType.str, 'filter-ref')),
                ('subtree_filter', YLeaf(YType.str, 'ietf-yang-push:subtree-filter')),
                ('xpath_filter', YLeaf(YType.str, 'ietf-yang-push:xpath-filter')),
                ('starttime', YLeaf(YType.str, 'startTime')),
                ('stoptime', YLeaf(YType.str, 'stopTime')),
                ('source_interface', YLeaf(YType.str, 'source-interface')),
                ('source_vrf', YLeaf(YType.uint32, 'source-vrf')),
                ('source_address', YLeaf(YType.str, 'source-address')),
                ('period', YLeaf(YType.uint32, 'ietf-yang-push:period')),
                ('anchor_time', YLeaf(YType.str, 'ietf-yang-push:anchor-time')),
                ('no_synch_on_start', YLeaf(YType.empty, 'ietf-yang-push:no-synch-on-start')),
                ('dampening_period', YLeaf(YType.uint32, 'ietf-yang-push:dampening-period')),
                ('excluded_change', YLeafList(YType.enumeration, 'ietf-yang-push:excluded-change')),
                ('dscp', YLeaf(YType.uint8, 'ietf-yang-push:dscp')),
                ('subscription_priority', YLeaf(YType.uint8, 'ietf-yang-push:subscription-priority')),
                ('subscription_dependency', YLeaf(YType.str, 'ietf-yang-push:subscription-dependency')),
            ])
            self.subscription_id = None
            self.configured_subscription = None
            self.subscription_status = None
            self.stream = None
            self.encoding = None
            self.filter = None
            self.filter_ref = None
            self.subtree_filter = None
            self.xpath_filter = None
            self.starttime = None
            self.stoptime = None
            self.source_interface = None
            self.source_vrf = None
            self.source_address = None
            self.period = None
            self.anchor_time = None
            self.no_synch_on_start = None
            self.dampening_period = None
            self.excluded_change = []
            self.dscp = None
            self.subscription_priority = None
            self.subscription_dependency = None

            self.receivers = Subscriptions.Subscription.Receivers()
            self.receivers.parent = self
            self._children_name_map["receivers"] = "receivers"
            self._children_yang_names.add("receivers")
            self._segment_path = lambda: "subscription" + "[subscription-id='" + str(self.subscription_id) + "']"
            self._absolute_path = lambda: "ietf-event-notifications:subscriptions/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Subscriptions.Subscription, ['subscription_id', 'configured_subscription', 'subscription_status', 'stream', 'encoding', 'filter', 'filter_ref', 'subtree_filter', 'xpath_filter', 'starttime', 'stoptime', 'source_interface', 'source_vrf', 'source_address', 'period', 'anchor_time', 'no_synch_on_start', 'dampening_period', 'excluded_change', 'dscp', 'subscription_priority', 'subscription_dependency'], name, value)


        class Receivers(Entity):
            """
            Set of receivers in a subscription.
            
            .. attribute:: receiver
            
            	A single host or multipoint address intended as a target for the notifications for a subscription
            	**type**\: list of  		 :py:class:`Receiver <ydk.models.ietf.ietf_event_notifications.Subscriptions.Subscription.Receivers.Receiver>`
            
            

            """

            _prefix = 'notif-bis'
            _revision = '2016-10-27'

            def __init__(self):
                super(Subscriptions.Subscription.Receivers, self).__init__()

                self.yang_name = "receivers"
                self.yang_parent_name = "subscription"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("receiver", ("receiver", Subscriptions.Subscription.Receivers.Receiver))])
                self._leafs = OrderedDict()

                self.receiver = YList(self)
                self._segment_path = lambda: "receivers"

            def __setattr__(self, name, value):
                self._perform_setattr(Subscriptions.Subscription.Receivers, [], name, value)


            class Receiver(Entity):
                """
                A single host or multipoint address intended as a target
                for the notifications for a subscription.
                
                .. attribute:: address  (key)
                
                	Specifies the address for the traffic to reach a remote host. One of the following must be specified\: an ipv4 address, an ipv6 address, or a host name
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
                
                	**mandatory**\: True
                
                .. attribute:: port
                
                	This leaf specifies the port number to use for messages destined for a receiver
                	**type**\: int
                
                	**range:** 0..65535
                
                	**mandatory**\: True
                
                .. attribute:: protocol
                
                	This leaf specifies the transport protocol used to deliver messages destined for the receiver
                	**type**\:  :py:class:`Transport <ydk.models.ietf.ietf_event_notifications.Transport>`
                
                	**default value**\: netconf
                
                

                """

                _prefix = 'notif-bis'
                _revision = '2016-10-27'

                def __init__(self):
                    super(Subscriptions.Subscription.Receivers.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "receivers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['address']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address', YLeaf(YType.str, 'address')),
                        ('port', YLeaf(YType.uint16, 'port')),
                        ('protocol', YLeaf(YType.identityref, 'protocol')),
                    ])
                    self.address = None
                    self.port = None
                    self.protocol = None
                    self._segment_path = lambda: "receiver" + "[address='" + str(self.address) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Subscriptions.Subscription.Receivers.Receiver, ['address', 'port', 'protocol'], name, value)

    def clone_ptr(self):
        self._top_entity = Subscriptions()
        return self._top_entity

class NETCONF(Identity):
    """
    Default NETCONF event stream, containing events based on
    notifications defined as YANG modules that are supported
    by the system.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(NETCONF, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:NETCONF")


class Ok(Identity):
    """
    OK \- RPC was successful and was performed as requested.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Ok, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:ok")


class Error(Identity):
    """
    RPC was not successful.
    Base identity for error return codes.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Error, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error")


class ErrorNoSuchSubscription(Identity):
    """
    A subscription with the requested subscription ID
    does not exist.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ErrorNoSuchSubscription, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error-no-such-subscription")


class ErrorNoSuchOption(Identity):
    """
    A requested parameter setting is not supported.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ErrorNoSuchOption, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error-no-such-option")


class ErrorInsufficientResources(Identity):
    """
    The publisher has insufficient resources to support the
    subscription as requested.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ErrorInsufficientResources, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error-insufficient-resources")


class ErrorConfiguredSubscription(Identity):
    """
    Cannot apply RPC to a configured subscription, i.e.
    to a subscription that was not established via RPC.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ErrorConfiguredSubscription, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error-configured-subscription")


class ErrorOther(Identity):
    """
    An unspecified error has occurred (catch all).
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ErrorOther, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error-other")


class Active(Identity):
    """
    Status is active and healthy.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Active, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:active")


class Inactive(Identity):
    """
    Status is inactive, for example outside the
    interval between start time and stop time.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Inactive, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:inactive")


class Suspended(Identity):
    """
    The status is suspended, meaning that the publisher
    is currently unable to provide the negotiated updates
    for the subscription.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Suspended, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:suspended")


class InError(Identity):
    """
    The status is in error or degraded, meaning that
    stream and/or subscription is currently unable to provide
    the negotiated notifications.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(InError, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:in-error")


class InternalError(Identity):
    """
    Subscription failures caused by server internal error.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(InternalError, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:internal-error")


class NoResources(Identity):
    """
    Lack of resources, e.g. CPU, memory, bandwidth
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(NoResources, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:no-resources")


class SubscriptionDeleted(Identity):
    """
    The subscription was terminated because the subscription
    was deleted.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(SubscriptionDeleted, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:subscription-deleted")


class Other(Identity):
    """
    Fallback reason \- any other reason
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Other, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:other")


class EncodeXml(Identity):
    """
    Encode data using XML
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(EncodeXml, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:encode-xml")


class EncodeJson(Identity):
    """
    Encode data using JSON
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(EncodeJson, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:encode-json")


class Netconf(Identity):
    """
    Netconf notifications as a transport.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Netconf, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:netconf")


