""" ietf_event_notifications 

This module contains conceptual YANG specifications
for NETCONF Event Notifications.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PushSource(Enum):
    """
    PushSource

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


class SubscriptionStreamStatus(Identity):
    """
    Base identity for the status of subscriptions and
    datastreams.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(SubscriptionStreamStatus, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:subscription-stream-status")


class Stream(Identity):
    """
    Base identity to represent a generic stream of event
    notifications.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Stream, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:stream")


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
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_event_notifications.EstablishSubscription.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_event_notifications.EstablishSubscription.Output>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(EstablishSubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "establish-subscription"
        self.yang_parent_name = "ietf-event-notifications"

        self.input = EstablishSubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = EstablishSubscription.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\:  int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\:  list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\:  str
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\:  anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\:  str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(EstablishSubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "establish-subscription"

            self.anchor_time = YLeaf(YType.str, "ietf-yang-push:anchor-time")

            self.dampening_period = YLeaf(YType.uint32, "ietf-yang-push:dampening-period")

            self.dscp = YLeaf(YType.uint8, "ietf-yang-push:dscp")

            self.encoding = YLeaf(YType.identityref, "encoding")

            self.excluded_change = YLeafList(YType.enumeration, "ietf-yang-push:excluded-change")

            self.filter = YLeaf(YType.str, "filter")

            self.filter_ref = YLeaf(YType.str, "filter-ref")

            self.no_synch_on_start = YLeaf(YType.empty, "ietf-yang-push:no-synch-on-start")

            self.period = YLeaf(YType.uint32, "ietf-yang-push:period")

            self.starttime = YLeaf(YType.str, "startTime")

            self.stoptime = YLeaf(YType.str, "stopTime")

            self.stream = YLeaf(YType.identityref, "stream")

            self.subscription_dependency = YLeaf(YType.str, "ietf-yang-push:subscription-dependency")

            self.subscription_priority = YLeaf(YType.uint8, "ietf-yang-push:subscription-priority")

            self.subtree_filter = YLeaf(YType.str, "ietf-yang-push:subtree-filter")

            self.xpath_filter = YLeaf(YType.str, "ietf-yang-push:xpath-filter")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("anchor_time",
                            "dampening_period",
                            "dscp",
                            "encoding",
                            "excluded_change",
                            "filter",
                            "filter_ref",
                            "no_synch_on_start",
                            "period",
                            "starttime",
                            "stoptime",
                            "stream",
                            "subscription_dependency",
                            "subscription_priority",
                            "subtree_filter",
                            "xpath_filter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EstablishSubscription.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EstablishSubscription.Input, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.anchor_time.is_set or
                self.dampening_period.is_set or
                self.dscp.is_set or
                self.encoding.is_set or
                self.filter.is_set or
                self.filter_ref.is_set or
                self.no_synch_on_start.is_set or
                self.period.is_set or
                self.starttime.is_set or
                self.stoptime.is_set or
                self.stream.is_set or
                self.subscription_dependency.is_set or
                self.subscription_priority.is_set or
                self.subtree_filter.is_set or
                self.xpath_filter.is_set)

        def has_operation(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.anchor_time.yfilter != YFilter.not_set or
                self.dampening_period.yfilter != YFilter.not_set or
                self.dscp.yfilter != YFilter.not_set or
                self.encoding.yfilter != YFilter.not_set or
                self.excluded_change.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.filter_ref.yfilter != YFilter.not_set or
                self.no_synch_on_start.yfilter != YFilter.not_set or
                self.period.yfilter != YFilter.not_set or
                self.starttime.yfilter != YFilter.not_set or
                self.stoptime.yfilter != YFilter.not_set or
                self.stream.yfilter != YFilter.not_set or
                self.subscription_dependency.yfilter != YFilter.not_set or
                self.subscription_priority.yfilter != YFilter.not_set or
                self.subtree_filter.yfilter != YFilter.not_set or
                self.xpath_filter.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:establish-subscription/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.anchor_time.is_set or self.anchor_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.anchor_time.get_name_leafdata())
            if (self.dampening_period.is_set or self.dampening_period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dampening_period.get_name_leafdata())
            if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dscp.get_name_leafdata())
            if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.encoding.get_name_leafdata())
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.filter_ref.is_set or self.filter_ref.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter_ref.get_name_leafdata())
            if (self.no_synch_on_start.is_set or self.no_synch_on_start.yfilter != YFilter.not_set):
                leaf_name_data.append(self.no_synch_on_start.get_name_leafdata())
            if (self.period.is_set or self.period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.period.get_name_leafdata())
            if (self.starttime.is_set or self.starttime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.starttime.get_name_leafdata())
            if (self.stoptime.is_set or self.stoptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stoptime.get_name_leafdata())
            if (self.stream.is_set or self.stream.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stream.get_name_leafdata())
            if (self.subscription_dependency.is_set or self.subscription_dependency.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_dependency.get_name_leafdata())
            if (self.subscription_priority.is_set or self.subscription_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_priority.get_name_leafdata())
            if (self.subtree_filter.is_set or self.subtree_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subtree_filter.get_name_leafdata())
            if (self.xpath_filter.is_set or self.xpath_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.xpath_filter.get_name_leafdata())

            leaf_name_data.extend(self.excluded_change.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "anchor-time" or name == "dampening-period" or name == "dscp" or name == "encoding" or name == "excluded-change" or name == "filter" or name == "filter-ref" or name == "no-synch-on-start" or name == "period" or name == "startTime" or name == "stopTime" or name == "stream" or name == "subscription-dependency" or name == "subscription-priority" or name == "subtree-filter" or name == "xpath-filter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "anchor-time"):
                self.anchor_time = value
                self.anchor_time.value_namespace = name_space
                self.anchor_time.value_namespace_prefix = name_space_prefix
            if(value_path == "dampening-period"):
                self.dampening_period = value
                self.dampening_period.value_namespace = name_space
                self.dampening_period.value_namespace_prefix = name_space_prefix
            if(value_path == "dscp"):
                self.dscp = value
                self.dscp.value_namespace = name_space
                self.dscp.value_namespace_prefix = name_space_prefix
            if(value_path == "encoding"):
                self.encoding = value
                self.encoding.value_namespace = name_space
                self.encoding.value_namespace_prefix = name_space_prefix
            if(value_path == "excluded-change"):
                self.excluded_change.append(value)
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "filter-ref"):
                self.filter_ref = value
                self.filter_ref.value_namespace = name_space
                self.filter_ref.value_namespace_prefix = name_space_prefix
            if(value_path == "no-synch-on-start"):
                self.no_synch_on_start = value
                self.no_synch_on_start.value_namespace = name_space
                self.no_synch_on_start.value_namespace_prefix = name_space_prefix
            if(value_path == "period"):
                self.period = value
                self.period.value_namespace = name_space
                self.period.value_namespace_prefix = name_space_prefix
            if(value_path == "startTime"):
                self.starttime = value
                self.starttime.value_namespace = name_space
                self.starttime.value_namespace_prefix = name_space_prefix
            if(value_path == "stopTime"):
                self.stoptime = value
                self.stoptime.value_namespace = name_space
                self.stoptime.value_namespace_prefix = name_space_prefix
            if(value_path == "stream"):
                self.stream = value
                self.stream.value_namespace = name_space
                self.stream.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-dependency"):
                self.subscription_dependency = value
                self.subscription_dependency.value_namespace = name_space
                self.subscription_dependency.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-priority"):
                self.subscription_priority = value
                self.subscription_priority.value_namespace = name_space
                self.subscription_priority.value_namespace_prefix = name_space_prefix
            if(value_path == "subtree-filter"):
                self.subtree_filter = value
                self.subtree_filter.value_namespace = name_space
                self.subtree_filter.value_namespace_prefix = name_space_prefix
            if(value_path == "xpath-filter"):
                self.xpath_filter = value
                self.xpath_filter.value_namespace = name_space
                self.xpath_filter.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\:  int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\:  list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\:  str
        
        .. attribute:: subscription_id
        
        	Identifier used for this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:   :py:class:`SubscriptionResult <ydk.models.ietf.ietf_event_notifications.SubscriptionResult>`
        
        	**mandatory**\: True
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\:  anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\:  str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(EstablishSubscription.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "establish-subscription"

            self.anchor_time = YLeaf(YType.str, "ietf-yang-push:anchor-time")

            self.dampening_period = YLeaf(YType.uint32, "ietf-yang-push:dampening-period")

            self.dscp = YLeaf(YType.uint8, "ietf-yang-push:dscp")

            self.encoding = YLeaf(YType.identityref, "encoding")

            self.excluded_change = YLeafList(YType.enumeration, "ietf-yang-push:excluded-change")

            self.filter = YLeaf(YType.str, "filter")

            self.filter_ref = YLeaf(YType.str, "filter-ref")

            self.no_synch_on_start = YLeaf(YType.empty, "ietf-yang-push:no-synch-on-start")

            self.period = YLeaf(YType.uint32, "ietf-yang-push:period")

            self.starttime = YLeaf(YType.str, "startTime")

            self.stoptime = YLeaf(YType.str, "stopTime")

            self.stream = YLeaf(YType.identityref, "stream")

            self.subscription_dependency = YLeaf(YType.str, "ietf-yang-push:subscription-dependency")

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.subscription_priority = YLeaf(YType.uint8, "ietf-yang-push:subscription-priority")

            self.subscription_result = YLeaf(YType.identityref, "subscription-result")

            self.subtree_filter = YLeaf(YType.str, "ietf-yang-push:subtree-filter")

            self.xpath_filter = YLeaf(YType.str, "ietf-yang-push:xpath-filter")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("anchor_time",
                            "dampening_period",
                            "dscp",
                            "encoding",
                            "excluded_change",
                            "filter",
                            "filter_ref",
                            "no_synch_on_start",
                            "period",
                            "starttime",
                            "stoptime",
                            "stream",
                            "subscription_dependency",
                            "subscription_id",
                            "subscription_priority",
                            "subscription_result",
                            "subtree_filter",
                            "xpath_filter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EstablishSubscription.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EstablishSubscription.Output, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.anchor_time.is_set or
                self.dampening_period.is_set or
                self.dscp.is_set or
                self.encoding.is_set or
                self.filter.is_set or
                self.filter_ref.is_set or
                self.no_synch_on_start.is_set or
                self.period.is_set or
                self.starttime.is_set or
                self.stoptime.is_set or
                self.stream.is_set or
                self.subscription_dependency.is_set or
                self.subscription_id.is_set or
                self.subscription_priority.is_set or
                self.subscription_result.is_set or
                self.subtree_filter.is_set or
                self.xpath_filter.is_set)

        def has_operation(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.anchor_time.yfilter != YFilter.not_set or
                self.dampening_period.yfilter != YFilter.not_set or
                self.dscp.yfilter != YFilter.not_set or
                self.encoding.yfilter != YFilter.not_set or
                self.excluded_change.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.filter_ref.yfilter != YFilter.not_set or
                self.no_synch_on_start.yfilter != YFilter.not_set or
                self.period.yfilter != YFilter.not_set or
                self.starttime.yfilter != YFilter.not_set or
                self.stoptime.yfilter != YFilter.not_set or
                self.stream.yfilter != YFilter.not_set or
                self.subscription_dependency.yfilter != YFilter.not_set or
                self.subscription_id.yfilter != YFilter.not_set or
                self.subscription_priority.yfilter != YFilter.not_set or
                self.subscription_result.yfilter != YFilter.not_set or
                self.subtree_filter.yfilter != YFilter.not_set or
                self.xpath_filter.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:establish-subscription/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.anchor_time.is_set or self.anchor_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.anchor_time.get_name_leafdata())
            if (self.dampening_period.is_set or self.dampening_period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dampening_period.get_name_leafdata())
            if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dscp.get_name_leafdata())
            if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.encoding.get_name_leafdata())
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.filter_ref.is_set or self.filter_ref.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter_ref.get_name_leafdata())
            if (self.no_synch_on_start.is_set or self.no_synch_on_start.yfilter != YFilter.not_set):
                leaf_name_data.append(self.no_synch_on_start.get_name_leafdata())
            if (self.period.is_set or self.period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.period.get_name_leafdata())
            if (self.starttime.is_set or self.starttime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.starttime.get_name_leafdata())
            if (self.stoptime.is_set or self.stoptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stoptime.get_name_leafdata())
            if (self.stream.is_set or self.stream.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stream.get_name_leafdata())
            if (self.subscription_dependency.is_set or self.subscription_dependency.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_dependency.get_name_leafdata())
            if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_id.get_name_leafdata())
            if (self.subscription_priority.is_set or self.subscription_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_priority.get_name_leafdata())
            if (self.subscription_result.is_set or self.subscription_result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_result.get_name_leafdata())
            if (self.subtree_filter.is_set or self.subtree_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subtree_filter.get_name_leafdata())
            if (self.xpath_filter.is_set or self.xpath_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.xpath_filter.get_name_leafdata())

            leaf_name_data.extend(self.excluded_change.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "anchor-time" or name == "dampening-period" or name == "dscp" or name == "encoding" or name == "excluded-change" or name == "filter" or name == "filter-ref" or name == "no-synch-on-start" or name == "period" or name == "startTime" or name == "stopTime" or name == "stream" or name == "subscription-dependency" or name == "subscription-id" or name == "subscription-priority" or name == "subscription-result" or name == "subtree-filter" or name == "xpath-filter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "anchor-time"):
                self.anchor_time = value
                self.anchor_time.value_namespace = name_space
                self.anchor_time.value_namespace_prefix = name_space_prefix
            if(value_path == "dampening-period"):
                self.dampening_period = value
                self.dampening_period.value_namespace = name_space
                self.dampening_period.value_namespace_prefix = name_space_prefix
            if(value_path == "dscp"):
                self.dscp = value
                self.dscp.value_namespace = name_space
                self.dscp.value_namespace_prefix = name_space_prefix
            if(value_path == "encoding"):
                self.encoding = value
                self.encoding.value_namespace = name_space
                self.encoding.value_namespace_prefix = name_space_prefix
            if(value_path == "excluded-change"):
                self.excluded_change.append(value)
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "filter-ref"):
                self.filter_ref = value
                self.filter_ref.value_namespace = name_space
                self.filter_ref.value_namespace_prefix = name_space_prefix
            if(value_path == "no-synch-on-start"):
                self.no_synch_on_start = value
                self.no_synch_on_start.value_namespace = name_space
                self.no_synch_on_start.value_namespace_prefix = name_space_prefix
            if(value_path == "period"):
                self.period = value
                self.period.value_namespace = name_space
                self.period.value_namespace_prefix = name_space_prefix
            if(value_path == "startTime"):
                self.starttime = value
                self.starttime.value_namespace = name_space
                self.starttime.value_namespace_prefix = name_space_prefix
            if(value_path == "stopTime"):
                self.stoptime = value
                self.stoptime.value_namespace = name_space
                self.stoptime.value_namespace_prefix = name_space_prefix
            if(value_path == "stream"):
                self.stream = value
                self.stream.value_namespace = name_space
                self.stream.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-dependency"):
                self.subscription_dependency = value
                self.subscription_dependency.value_namespace = name_space
                self.subscription_dependency.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-id"):
                self.subscription_id = value
                self.subscription_id.value_namespace = name_space
                self.subscription_id.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-priority"):
                self.subscription_priority = value
                self.subscription_priority.value_namespace = name_space
                self.subscription_priority.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-result"):
                self.subscription_result = value
                self.subscription_result.value_namespace = name_space
                self.subscription_result.value_namespace_prefix = name_space_prefix
            if(value_path == "subtree-filter"):
                self.subtree_filter = value
                self.subtree_filter.value_namespace = name_space
                self.subtree_filter.value_namespace_prefix = name_space_prefix
            if(value_path == "xpath-filter"):
                self.xpath_filter = value
                self.xpath_filter.value_namespace = name_space
                self.xpath_filter.value_namespace_prefix = name_space_prefix

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
        path_buffer = "ietf-event-notifications:establish-subscription" + path_buffer

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
                self.input = EstablishSubscription.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = EstablishSubscription.Output()
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
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_event_notifications.CreateSubscription.Input>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(CreateSubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "create-subscription"
        self.yang_parent_name = "ietf-event-notifications"

        self.input = CreateSubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\:  anyxml
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        	**default value**\: NETCONF
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(CreateSubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "create-subscription"

            self.encoding = YLeaf(YType.identityref, "encoding")

            self.filter = YLeaf(YType.str, "filter")

            self.starttime = YLeaf(YType.str, "startTime")

            self.stoptime = YLeaf(YType.str, "stopTime")

            self.stream = YLeaf(YType.identityref, "stream")

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
                            "filter",
                            "starttime",
                            "stoptime",
                            "stream") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CreateSubscription.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CreateSubscription.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.encoding.is_set or
                self.filter.is_set or
                self.starttime.is_set or
                self.stoptime.is_set or
                self.stream.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.encoding.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.starttime.yfilter != YFilter.not_set or
                self.stoptime.yfilter != YFilter.not_set or
                self.stream.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:create-subscription/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.encoding.get_name_leafdata())
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.starttime.is_set or self.starttime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.starttime.get_name_leafdata())
            if (self.stoptime.is_set or self.stoptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stoptime.get_name_leafdata())
            if (self.stream.is_set or self.stream.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stream.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "encoding" or name == "filter" or name == "startTime" or name == "stopTime" or name == "stream"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "encoding"):
                self.encoding = value
                self.encoding.value_namespace = name_space
                self.encoding.value_namespace_prefix = name_space_prefix
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "startTime"):
                self.starttime = value
                self.starttime.value_namespace = name_space
                self.starttime.value_namespace_prefix = name_space_prefix
            if(value_path == "stopTime"):
                self.stoptime = value
                self.stoptime.value_namespace = name_space
                self.stoptime.value_namespace_prefix = name_space_prefix
            if(value_path == "stream"):
                self.stream = value
                self.stream.value_namespace = name_space
                self.stream.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-event-notifications:create-subscription" + path_buffer

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
                self.input = CreateSubscription.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_event_notifications.ModifySubscription.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_event_notifications.ModifySubscription.Output>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ModifySubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "modify-subscription"
        self.yang_parent_name = "ietf-event-notifications"

        self.input = ModifySubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = ModifySubscription.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\:  list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: subscription_id
        
        	Identifier to use for this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\:  anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\:  str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(ModifySubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "modify-subscription"

            self.anchor_time = YLeaf(YType.str, "ietf-yang-push:anchor-time")

            self.dampening_period = YLeaf(YType.uint32, "ietf-yang-push:dampening-period")

            self.excluded_change = YLeafList(YType.enumeration, "ietf-yang-push:excluded-change")

            self.filter = YLeaf(YType.str, "filter")

            self.filter_ref = YLeaf(YType.str, "filter-ref")

            self.no_synch_on_start = YLeaf(YType.empty, "ietf-yang-push:no-synch-on-start")

            self.period = YLeaf(YType.uint32, "ietf-yang-push:period")

            self.starttime = YLeaf(YType.str, "startTime")

            self.stoptime = YLeaf(YType.str, "stopTime")

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.subtree_filter = YLeaf(YType.str, "ietf-yang-push:subtree-filter")

            self.xpath_filter = YLeaf(YType.str, "ietf-yang-push:xpath-filter")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("anchor_time",
                            "dampening_period",
                            "excluded_change",
                            "filter",
                            "filter_ref",
                            "no_synch_on_start",
                            "period",
                            "starttime",
                            "stoptime",
                            "subscription_id",
                            "subtree_filter",
                            "xpath_filter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ModifySubscription.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ModifySubscription.Input, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.anchor_time.is_set or
                self.dampening_period.is_set or
                self.filter.is_set or
                self.filter_ref.is_set or
                self.no_synch_on_start.is_set or
                self.period.is_set or
                self.starttime.is_set or
                self.stoptime.is_set or
                self.subscription_id.is_set or
                self.subtree_filter.is_set or
                self.xpath_filter.is_set)

        def has_operation(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.anchor_time.yfilter != YFilter.not_set or
                self.dampening_period.yfilter != YFilter.not_set or
                self.excluded_change.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.filter_ref.yfilter != YFilter.not_set or
                self.no_synch_on_start.yfilter != YFilter.not_set or
                self.period.yfilter != YFilter.not_set or
                self.starttime.yfilter != YFilter.not_set or
                self.stoptime.yfilter != YFilter.not_set or
                self.subscription_id.yfilter != YFilter.not_set or
                self.subtree_filter.yfilter != YFilter.not_set or
                self.xpath_filter.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:modify-subscription/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.anchor_time.is_set or self.anchor_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.anchor_time.get_name_leafdata())
            if (self.dampening_period.is_set or self.dampening_period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dampening_period.get_name_leafdata())
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.filter_ref.is_set or self.filter_ref.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter_ref.get_name_leafdata())
            if (self.no_synch_on_start.is_set or self.no_synch_on_start.yfilter != YFilter.not_set):
                leaf_name_data.append(self.no_synch_on_start.get_name_leafdata())
            if (self.period.is_set or self.period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.period.get_name_leafdata())
            if (self.starttime.is_set or self.starttime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.starttime.get_name_leafdata())
            if (self.stoptime.is_set or self.stoptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stoptime.get_name_leafdata())
            if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_id.get_name_leafdata())
            if (self.subtree_filter.is_set or self.subtree_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subtree_filter.get_name_leafdata())
            if (self.xpath_filter.is_set or self.xpath_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.xpath_filter.get_name_leafdata())

            leaf_name_data.extend(self.excluded_change.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "anchor-time" or name == "dampening-period" or name == "excluded-change" or name == "filter" or name == "filter-ref" or name == "no-synch-on-start" or name == "period" or name == "startTime" or name == "stopTime" or name == "subscription-id" or name == "subtree-filter" or name == "xpath-filter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "anchor-time"):
                self.anchor_time = value
                self.anchor_time.value_namespace = name_space
                self.anchor_time.value_namespace_prefix = name_space_prefix
            if(value_path == "dampening-period"):
                self.dampening_period = value
                self.dampening_period.value_namespace = name_space
                self.dampening_period.value_namespace_prefix = name_space_prefix
            if(value_path == "excluded-change"):
                self.excluded_change.append(value)
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "filter-ref"):
                self.filter_ref = value
                self.filter_ref.value_namespace = name_space
                self.filter_ref.value_namespace_prefix = name_space_prefix
            if(value_path == "no-synch-on-start"):
                self.no_synch_on_start = value
                self.no_synch_on_start.value_namespace = name_space
                self.no_synch_on_start.value_namespace_prefix = name_space_prefix
            if(value_path == "period"):
                self.period = value
                self.period.value_namespace = name_space
                self.period.value_namespace_prefix = name_space_prefix
            if(value_path == "startTime"):
                self.starttime = value
                self.starttime.value_namespace = name_space
                self.starttime.value_namespace_prefix = name_space_prefix
            if(value_path == "stopTime"):
                self.stoptime = value
                self.stoptime.value_namespace = name_space
                self.stoptime.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-id"):
                self.subscription_id = value
                self.subscription_id.value_namespace = name_space
                self.subscription_id.value_namespace_prefix = name_space_prefix
            if(value_path == "subtree-filter"):
                self.subtree_filter = value
                self.subtree_filter.value_namespace = name_space
                self.subtree_filter.value_namespace_prefix = name_space_prefix
            if(value_path == "xpath-filter"):
                self.xpath_filter = value
                self.xpath_filter.value_namespace = name_space
                self.xpath_filter.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\:  int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\:  list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\:  str
        
        .. attribute:: subscription_id
        
        	Identifier used for this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:   :py:class:`SubscriptionResult <ydk.models.ietf.ietf_event_notifications.SubscriptionResult>`
        
        	**mandatory**\: True
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\:  anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\:  str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(ModifySubscription.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "modify-subscription"

            self.anchor_time = YLeaf(YType.str, "ietf-yang-push:anchor-time")

            self.dampening_period = YLeaf(YType.uint32, "ietf-yang-push:dampening-period")

            self.dscp = YLeaf(YType.uint8, "ietf-yang-push:dscp")

            self.encoding = YLeaf(YType.identityref, "encoding")

            self.excluded_change = YLeafList(YType.enumeration, "ietf-yang-push:excluded-change")

            self.filter = YLeaf(YType.str, "filter")

            self.filter_ref = YLeaf(YType.str, "filter-ref")

            self.no_synch_on_start = YLeaf(YType.empty, "ietf-yang-push:no-synch-on-start")

            self.period = YLeaf(YType.uint32, "ietf-yang-push:period")

            self.starttime = YLeaf(YType.str, "startTime")

            self.stoptime = YLeaf(YType.str, "stopTime")

            self.stream = YLeaf(YType.identityref, "stream")

            self.subscription_dependency = YLeaf(YType.str, "ietf-yang-push:subscription-dependency")

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.subscription_priority = YLeaf(YType.uint8, "ietf-yang-push:subscription-priority")

            self.subscription_result = YLeaf(YType.identityref, "subscription-result")

            self.subtree_filter = YLeaf(YType.str, "ietf-yang-push:subtree-filter")

            self.xpath_filter = YLeaf(YType.str, "ietf-yang-push:xpath-filter")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("anchor_time",
                            "dampening_period",
                            "dscp",
                            "encoding",
                            "excluded_change",
                            "filter",
                            "filter_ref",
                            "no_synch_on_start",
                            "period",
                            "starttime",
                            "stoptime",
                            "stream",
                            "subscription_dependency",
                            "subscription_id",
                            "subscription_priority",
                            "subscription_result",
                            "subtree_filter",
                            "xpath_filter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ModifySubscription.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ModifySubscription.Output, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.anchor_time.is_set or
                self.dampening_period.is_set or
                self.dscp.is_set or
                self.encoding.is_set or
                self.filter.is_set or
                self.filter_ref.is_set or
                self.no_synch_on_start.is_set or
                self.period.is_set or
                self.starttime.is_set or
                self.stoptime.is_set or
                self.stream.is_set or
                self.subscription_dependency.is_set or
                self.subscription_id.is_set or
                self.subscription_priority.is_set or
                self.subscription_result.is_set or
                self.subtree_filter.is_set or
                self.xpath_filter.is_set)

        def has_operation(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.anchor_time.yfilter != YFilter.not_set or
                self.dampening_period.yfilter != YFilter.not_set or
                self.dscp.yfilter != YFilter.not_set or
                self.encoding.yfilter != YFilter.not_set or
                self.excluded_change.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.filter_ref.yfilter != YFilter.not_set or
                self.no_synch_on_start.yfilter != YFilter.not_set or
                self.period.yfilter != YFilter.not_set or
                self.starttime.yfilter != YFilter.not_set or
                self.stoptime.yfilter != YFilter.not_set or
                self.stream.yfilter != YFilter.not_set or
                self.subscription_dependency.yfilter != YFilter.not_set or
                self.subscription_id.yfilter != YFilter.not_set or
                self.subscription_priority.yfilter != YFilter.not_set or
                self.subscription_result.yfilter != YFilter.not_set or
                self.subtree_filter.yfilter != YFilter.not_set or
                self.xpath_filter.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:modify-subscription/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.anchor_time.is_set or self.anchor_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.anchor_time.get_name_leafdata())
            if (self.dampening_period.is_set or self.dampening_period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dampening_period.get_name_leafdata())
            if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dscp.get_name_leafdata())
            if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.encoding.get_name_leafdata())
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.filter_ref.is_set or self.filter_ref.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter_ref.get_name_leafdata())
            if (self.no_synch_on_start.is_set or self.no_synch_on_start.yfilter != YFilter.not_set):
                leaf_name_data.append(self.no_synch_on_start.get_name_leafdata())
            if (self.period.is_set or self.period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.period.get_name_leafdata())
            if (self.starttime.is_set or self.starttime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.starttime.get_name_leafdata())
            if (self.stoptime.is_set or self.stoptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stoptime.get_name_leafdata())
            if (self.stream.is_set or self.stream.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stream.get_name_leafdata())
            if (self.subscription_dependency.is_set or self.subscription_dependency.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_dependency.get_name_leafdata())
            if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_id.get_name_leafdata())
            if (self.subscription_priority.is_set or self.subscription_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_priority.get_name_leafdata())
            if (self.subscription_result.is_set or self.subscription_result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_result.get_name_leafdata())
            if (self.subtree_filter.is_set or self.subtree_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subtree_filter.get_name_leafdata())
            if (self.xpath_filter.is_set or self.xpath_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.xpath_filter.get_name_leafdata())

            leaf_name_data.extend(self.excluded_change.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "anchor-time" or name == "dampening-period" or name == "dscp" or name == "encoding" or name == "excluded-change" or name == "filter" or name == "filter-ref" or name == "no-synch-on-start" or name == "period" or name == "startTime" or name == "stopTime" or name == "stream" or name == "subscription-dependency" or name == "subscription-id" or name == "subscription-priority" or name == "subscription-result" or name == "subtree-filter" or name == "xpath-filter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "anchor-time"):
                self.anchor_time = value
                self.anchor_time.value_namespace = name_space
                self.anchor_time.value_namespace_prefix = name_space_prefix
            if(value_path == "dampening-period"):
                self.dampening_period = value
                self.dampening_period.value_namespace = name_space
                self.dampening_period.value_namespace_prefix = name_space_prefix
            if(value_path == "dscp"):
                self.dscp = value
                self.dscp.value_namespace = name_space
                self.dscp.value_namespace_prefix = name_space_prefix
            if(value_path == "encoding"):
                self.encoding = value
                self.encoding.value_namespace = name_space
                self.encoding.value_namespace_prefix = name_space_prefix
            if(value_path == "excluded-change"):
                self.excluded_change.append(value)
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "filter-ref"):
                self.filter_ref = value
                self.filter_ref.value_namespace = name_space
                self.filter_ref.value_namespace_prefix = name_space_prefix
            if(value_path == "no-synch-on-start"):
                self.no_synch_on_start = value
                self.no_synch_on_start.value_namespace = name_space
                self.no_synch_on_start.value_namespace_prefix = name_space_prefix
            if(value_path == "period"):
                self.period = value
                self.period.value_namespace = name_space
                self.period.value_namespace_prefix = name_space_prefix
            if(value_path == "startTime"):
                self.starttime = value
                self.starttime.value_namespace = name_space
                self.starttime.value_namespace_prefix = name_space_prefix
            if(value_path == "stopTime"):
                self.stoptime = value
                self.stoptime.value_namespace = name_space
                self.stoptime.value_namespace_prefix = name_space_prefix
            if(value_path == "stream"):
                self.stream = value
                self.stream.value_namespace = name_space
                self.stream.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-dependency"):
                self.subscription_dependency = value
                self.subscription_dependency.value_namespace = name_space
                self.subscription_dependency.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-id"):
                self.subscription_id = value
                self.subscription_id.value_namespace = name_space
                self.subscription_id.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-priority"):
                self.subscription_priority = value
                self.subscription_priority.value_namespace = name_space
                self.subscription_priority.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-result"):
                self.subscription_result = value
                self.subscription_result.value_namespace = name_space
                self.subscription_result.value_namespace_prefix = name_space_prefix
            if(value_path == "subtree-filter"):
                self.subtree_filter = value
                self.subtree_filter.value_namespace = name_space
                self.subtree_filter.value_namespace_prefix = name_space_prefix
            if(value_path == "xpath-filter"):
                self.xpath_filter = value
                self.xpath_filter.value_namespace = name_space
                self.xpath_filter.value_namespace_prefix = name_space_prefix

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
        path_buffer = "ietf-event-notifications:modify-subscription" + path_buffer

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
                self.input = ModifySubscription.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = ModifySubscription.Output()
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
        self._top_entity = ModifySubscription()
        return self._top_entity

class DeleteSubscription(Entity):
    """
    This RPC allows a subscriber to delete a subscription that
    was previously created using establish\-subscription.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_event_notifications.DeleteSubscription.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_event_notifications.DeleteSubscription.Output>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(DeleteSubscription, self).__init__()
        self._top_entity = None

        self.yang_name = "delete-subscription"
        self.yang_parent_name = "ietf-event-notifications"

        self.input = DeleteSubscription.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = DeleteSubscription.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: subscription_id
        
        	Identifier of the subscription that is to be deleted. Only subscriptions that were created using establish\-subscription can be deleted via this RPC
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(DeleteSubscription.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "delete-subscription"

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("subscription_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DeleteSubscription.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DeleteSubscription.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.subscription_id.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.subscription_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:delete-subscription/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "subscription-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "subscription-id"):
                self.subscription_id = value
                self.subscription_id.value_namespace = name_space
                self.subscription_id.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:   :py:class:`SubscriptionResult <ydk.models.ietf.ietf_event_notifications.SubscriptionResult>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(DeleteSubscription.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "delete-subscription"

            self.subscription_result = YLeaf(YType.identityref, "subscription-result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("subscription_result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DeleteSubscription.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DeleteSubscription.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.subscription_result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.subscription_result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:delete-subscription/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.subscription_result.is_set or self.subscription_result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "subscription-result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "subscription-result"):
                self.subscription_result = value
                self.subscription_result.value_namespace = name_space
                self.subscription_result.value_namespace_prefix = name_space_prefix

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
        path_buffer = "ietf-event-notifications:delete-subscription" + path_buffer

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
                self.input = DeleteSubscription.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = DeleteSubscription.Output()
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
        self._top_entity = DeleteSubscription()
        return self._top_entity

class Streams(Entity):
    """
    This container contains a leaf list of built\-in
    streams that are provided by the system.
    
    .. attribute:: stream
    
    	Identifies the built\-in streams that are supported by the system.  Built\-in streams are associated with their own identities, each of which carries a special semantics. In case configurable custom streams are supported, as indicated by the custom\-stream identity, the configuration of those custom streams is provided         separately
    	**type**\:  
    		list of  
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Streams, self).__init__()
        self._top_entity = None

        self.yang_name = "streams"
        self.yang_parent_name = "ietf-event-notifications"

        self.stream = YLeafList(YType.identityref, "stream")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("stream") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Streams, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Streams, self).__setattr__(name, value)

    def has_data(self):
        for leaf in self.stream.getYLeafs():
            if (leaf.yfilter != YFilter.not_set):
                return True
        return False

    def has_operation(self):
        for leaf in self.stream.getYLeafs():
            if (leaf.is_set):
                return True
        return (
            self.yfilter != YFilter.not_set or
            self.stream.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-event-notifications:streams" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        leaf_name_data.extend(self.stream.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "stream"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "stream"):
            identity = Identity(name_space, name_space_prefix, value)
            self.stream.append(identity)

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
    	**type**\: list of    :py:class:`Filter <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Filters, self).__init__()
        self._top_entity = None

        self.yang_name = "filters"
        self.yang_parent_name = "ietf-event-notifications"

        self.filter = YList(self)

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
                    super(Filters, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Filters, self).__setattr__(name, value)


    class Filter(Entity):
        """
        A list of configurable filters that can be applied to
        subscriptions.
        
        .. attribute:: filter_id  <key>
        
        	An identifier to differentiate between filters
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\:  anyxml
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\:  anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\:  str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(Filters.Filter, self).__init__()

            self.yang_name = "filter"
            self.yang_parent_name = "filters"

            self.filter_id = YLeaf(YType.uint32, "filter-id")

            self.filter = YLeaf(YType.str, "filter")

            self.subtree_filter = YLeaf(YType.str, "ietf-yang-push:subtree-filter")

            self.xpath_filter = YLeaf(YType.str, "ietf-yang-push:xpath-filter")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("filter_id",
                            "filter",
                            "subtree_filter",
                            "xpath_filter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Filters.Filter, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Filters.Filter, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.filter_id.is_set or
                self.filter.is_set or
                self.subtree_filter.is_set or
                self.xpath_filter.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.filter_id.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.subtree_filter.yfilter != YFilter.not_set or
                self.xpath_filter.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "filter" + "[filter-id='" + self.filter_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:filters/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.filter_id.is_set or self.filter_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter_id.get_name_leafdata())
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.subtree_filter.is_set or self.subtree_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subtree_filter.get_name_leafdata())
            if (self.xpath_filter.is_set or self.xpath_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.xpath_filter.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "filter-id" or name == "filter" or name == "subtree-filter" or name == "xpath-filter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "filter-id"):
                self.filter_id = value
                self.filter_id.value_namespace = name_space
                self.filter_id.value_namespace_prefix = name_space_prefix
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "subtree-filter"):
                self.subtree_filter = value
                self.subtree_filter.value_namespace = name_space
                self.subtree_filter.value_namespace_prefix = name_space_prefix
            if(value_path == "xpath-filter"):
                self.xpath_filter = value
                self.xpath_filter.value_namespace = name_space
                self.xpath_filter.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.filter:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.filter:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-event-notifications:filters" + path_buffer

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

        if (child_yang_name == "filter"):
            for c in self.filter:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Filters.Filter()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.filter.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "filter"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Filters()
        return self._top_entity

class SubscriptionConfig(Entity):
    """
    Contains the list of subscriptions that are configured,
    as opposed to established via RPC or other means.
    
    .. attribute:: subscription
    
    	Content of a subscription
    	**type**\: list of    :py:class:`Subscription <ydk.models.ietf.ietf_event_notifications.SubscriptionConfig.Subscription>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(SubscriptionConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "subscription-config"
        self.yang_parent_name = "ietf-event-notifications"

        self.subscription = YList(self)

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
                    super(SubscriptionConfig, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(SubscriptionConfig, self).__setattr__(name, value)


    class Subscription(Entity):
        """
        Content of a subscription.
        
        .. attribute:: subscription_id  <key>
        
        	Identifier to use for this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\:  int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\:  list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: receivers
        
        	Set of receivers in a subscription
        	**type**\:   :py:class:`Receivers <ydk.models.ietf.ietf_event_notifications.SubscriptionConfig.Subscription.Receivers>`
        
        .. attribute:: source_address
        
        	The source address for the notifications
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        
        ----
        .. attribute:: source_interface
        
        	References the interface for notifications
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        .. attribute:: source_vrf
        
        	Label of the vrf
        	**type**\:  int
        
        	**range:** 16..1048574
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\:  str
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\:  anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\:  str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(SubscriptionConfig.Subscription, self).__init__()

            self.yang_name = "subscription"
            self.yang_parent_name = "subscription-config"

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.anchor_time = YLeaf(YType.str, "ietf-yang-push:anchor-time")

            self.dampening_period = YLeaf(YType.uint32, "ietf-yang-push:dampening-period")

            self.dscp = YLeaf(YType.uint8, "ietf-yang-push:dscp")

            self.encoding = YLeaf(YType.identityref, "encoding")

            self.excluded_change = YLeafList(YType.enumeration, "ietf-yang-push:excluded-change")

            self.filter = YLeaf(YType.str, "filter")

            self.filter_ref = YLeaf(YType.str, "filter-ref")

            self.no_synch_on_start = YLeaf(YType.empty, "ietf-yang-push:no-synch-on-start")

            self.period = YLeaf(YType.uint32, "ietf-yang-push:period")

            self.source_address = YLeaf(YType.str, "source-address")

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.source_vrf = YLeaf(YType.uint32, "source-vrf")

            self.starttime = YLeaf(YType.str, "startTime")

            self.stoptime = YLeaf(YType.str, "stopTime")

            self.stream = YLeaf(YType.identityref, "stream")

            self.subscription_dependency = YLeaf(YType.str, "ietf-yang-push:subscription-dependency")

            self.subscription_priority = YLeaf(YType.uint8, "ietf-yang-push:subscription-priority")

            self.subtree_filter = YLeaf(YType.str, "ietf-yang-push:subtree-filter")

            self.xpath_filter = YLeaf(YType.str, "ietf-yang-push:xpath-filter")

            self.receivers = SubscriptionConfig.Subscription.Receivers()
            self.receivers.parent = self
            self._children_name_map["receivers"] = "receivers"
            self._children_yang_names.add("receivers")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("subscription_id",
                            "anchor_time",
                            "dampening_period",
                            "dscp",
                            "encoding",
                            "excluded_change",
                            "filter",
                            "filter_ref",
                            "no_synch_on_start",
                            "period",
                            "source_address",
                            "source_interface",
                            "source_vrf",
                            "starttime",
                            "stoptime",
                            "stream",
                            "subscription_dependency",
                            "subscription_priority",
                            "subtree_filter",
                            "xpath_filter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SubscriptionConfig.Subscription, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SubscriptionConfig.Subscription, self).__setattr__(name, value)


        class Receivers(Entity):
            """
            Set of receivers in a subscription.
            
            .. attribute:: receiver
            
            	A single host or multipoint address intended as a target for the notifications for a subscription
            	**type**\: list of    :py:class:`Receiver <ydk.models.ietf.ietf_event_notifications.SubscriptionConfig.Subscription.Receivers.Receiver>`
            
            

            """

            _prefix = 'notif-bis'
            _revision = '2016-10-27'

            def __init__(self):
                super(SubscriptionConfig.Subscription.Receivers, self).__init__()

                self.yang_name = "receivers"
                self.yang_parent_name = "subscription"

                self.receiver = YList(self)

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
                            super(SubscriptionConfig.Subscription.Receivers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SubscriptionConfig.Subscription.Receivers, self).__setattr__(name, value)


            class Receiver(Entity):
                """
                A single host or multipoint address intended as a target
                for the notifications for a subscription.
                
                .. attribute:: address  <key>
                
                	Specifies the address for the traffic to reach a remote host. One of the following must be specified\: an ipv4 address, an ipv6 address, or a host name
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                
                ----
                	**type**\:  str
                
                	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: port
                
                	This leaf specifies the port number to use for messages destined for a receiver
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**mandatory**\: True
                
                .. attribute:: protocol
                
                	This leaf specifies the transport protocol used to deliver messages destined for the receiver
                	**type**\:   :py:class:`Transport <ydk.models.ietf.ietf_event_notifications.Transport>`
                
                	**default value**\: netconf
                
                

                """

                _prefix = 'notif-bis'
                _revision = '2016-10-27'

                def __init__(self):
                    super(SubscriptionConfig.Subscription.Receivers.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "receivers"

                    self.address = YLeaf(YType.str, "address")

                    self.port = YLeaf(YType.uint16, "port")

                    self.protocol = YLeaf(YType.identityref, "protocol")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address",
                                    "port",
                                    "protocol") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SubscriptionConfig.Subscription.Receivers.Receiver, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SubscriptionConfig.Subscription.Receivers.Receiver, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.port.is_set or
                        self.protocol.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.protocol.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "receiver" + "[address='" + self.address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "port" or name == "protocol"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol"):
                        self.protocol = value
                        self.protocol.value_namespace = name_space
                        self.protocol.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.receiver:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.receiver:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "receivers" + path_buffer

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

                if (child_yang_name == "receiver"):
                    for c in self.receiver:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = SubscriptionConfig.Subscription.Receivers.Receiver()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.receiver.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "receiver"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.subscription_id.is_set or
                self.anchor_time.is_set or
                self.dampening_period.is_set or
                self.dscp.is_set or
                self.encoding.is_set or
                self.filter.is_set or
                self.filter_ref.is_set or
                self.no_synch_on_start.is_set or
                self.period.is_set or
                self.source_address.is_set or
                self.source_interface.is_set or
                self.source_vrf.is_set or
                self.starttime.is_set or
                self.stoptime.is_set or
                self.stream.is_set or
                self.subscription_dependency.is_set or
                self.subscription_priority.is_set or
                self.subtree_filter.is_set or
                self.xpath_filter.is_set or
                (self.receivers is not None and self.receivers.has_data()))

        def has_operation(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.subscription_id.yfilter != YFilter.not_set or
                self.anchor_time.yfilter != YFilter.not_set or
                self.dampening_period.yfilter != YFilter.not_set or
                self.dscp.yfilter != YFilter.not_set or
                self.encoding.yfilter != YFilter.not_set or
                self.excluded_change.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.filter_ref.yfilter != YFilter.not_set or
                self.no_synch_on_start.yfilter != YFilter.not_set or
                self.period.yfilter != YFilter.not_set or
                self.source_address.yfilter != YFilter.not_set or
                self.source_interface.yfilter != YFilter.not_set or
                self.source_vrf.yfilter != YFilter.not_set or
                self.starttime.yfilter != YFilter.not_set or
                self.stoptime.yfilter != YFilter.not_set or
                self.stream.yfilter != YFilter.not_set or
                self.subscription_dependency.yfilter != YFilter.not_set or
                self.subscription_priority.yfilter != YFilter.not_set or
                self.subtree_filter.yfilter != YFilter.not_set or
                self.xpath_filter.yfilter != YFilter.not_set or
                (self.receivers is not None and self.receivers.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "subscription" + "[subscription-id='" + self.subscription_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:subscription-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_id.get_name_leafdata())
            if (self.anchor_time.is_set or self.anchor_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.anchor_time.get_name_leafdata())
            if (self.dampening_period.is_set or self.dampening_period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dampening_period.get_name_leafdata())
            if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dscp.get_name_leafdata())
            if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.encoding.get_name_leafdata())
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.filter_ref.is_set or self.filter_ref.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter_ref.get_name_leafdata())
            if (self.no_synch_on_start.is_set or self.no_synch_on_start.yfilter != YFilter.not_set):
                leaf_name_data.append(self.no_synch_on_start.get_name_leafdata())
            if (self.period.is_set or self.period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.period.get_name_leafdata())
            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_address.get_name_leafdata())
            if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface.get_name_leafdata())
            if (self.source_vrf.is_set or self.source_vrf.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_vrf.get_name_leafdata())
            if (self.starttime.is_set or self.starttime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.starttime.get_name_leafdata())
            if (self.stoptime.is_set or self.stoptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stoptime.get_name_leafdata())
            if (self.stream.is_set or self.stream.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stream.get_name_leafdata())
            if (self.subscription_dependency.is_set or self.subscription_dependency.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_dependency.get_name_leafdata())
            if (self.subscription_priority.is_set or self.subscription_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_priority.get_name_leafdata())
            if (self.subtree_filter.is_set or self.subtree_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subtree_filter.get_name_leafdata())
            if (self.xpath_filter.is_set or self.xpath_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.xpath_filter.get_name_leafdata())

            leaf_name_data.extend(self.excluded_change.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "receivers"):
                if (self.receivers is None):
                    self.receivers = SubscriptionConfig.Subscription.Receivers()
                    self.receivers.parent = self
                    self._children_name_map["receivers"] = "receivers"
                return self.receivers

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "receivers" or name == "subscription-id" or name == "anchor-time" or name == "dampening-period" or name == "dscp" or name == "encoding" or name == "excluded-change" or name == "filter" or name == "filter-ref" or name == "no-synch-on-start" or name == "period" or name == "source-address" or name == "source-interface" or name == "source-vrf" or name == "startTime" or name == "stopTime" or name == "stream" or name == "subscription-dependency" or name == "subscription-priority" or name == "subtree-filter" or name == "xpath-filter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "subscription-id"):
                self.subscription_id = value
                self.subscription_id.value_namespace = name_space
                self.subscription_id.value_namespace_prefix = name_space_prefix
            if(value_path == "anchor-time"):
                self.anchor_time = value
                self.anchor_time.value_namespace = name_space
                self.anchor_time.value_namespace_prefix = name_space_prefix
            if(value_path == "dampening-period"):
                self.dampening_period = value
                self.dampening_period.value_namespace = name_space
                self.dampening_period.value_namespace_prefix = name_space_prefix
            if(value_path == "dscp"):
                self.dscp = value
                self.dscp.value_namespace = name_space
                self.dscp.value_namespace_prefix = name_space_prefix
            if(value_path == "encoding"):
                self.encoding = value
                self.encoding.value_namespace = name_space
                self.encoding.value_namespace_prefix = name_space_prefix
            if(value_path == "excluded-change"):
                self.excluded_change.append(value)
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "filter-ref"):
                self.filter_ref = value
                self.filter_ref.value_namespace = name_space
                self.filter_ref.value_namespace_prefix = name_space_prefix
            if(value_path == "no-synch-on-start"):
                self.no_synch_on_start = value
                self.no_synch_on_start.value_namespace = name_space
                self.no_synch_on_start.value_namespace_prefix = name_space_prefix
            if(value_path == "period"):
                self.period = value
                self.period.value_namespace = name_space
                self.period.value_namespace_prefix = name_space_prefix
            if(value_path == "source-address"):
                self.source_address = value
                self.source_address.value_namespace = name_space
                self.source_address.value_namespace_prefix = name_space_prefix
            if(value_path == "source-interface"):
                self.source_interface = value
                self.source_interface.value_namespace = name_space
                self.source_interface.value_namespace_prefix = name_space_prefix
            if(value_path == "source-vrf"):
                self.source_vrf = value
                self.source_vrf.value_namespace = name_space
                self.source_vrf.value_namespace_prefix = name_space_prefix
            if(value_path == "startTime"):
                self.starttime = value
                self.starttime.value_namespace = name_space
                self.starttime.value_namespace_prefix = name_space_prefix
            if(value_path == "stopTime"):
                self.stoptime = value
                self.stoptime.value_namespace = name_space
                self.stoptime.value_namespace_prefix = name_space_prefix
            if(value_path == "stream"):
                self.stream = value
                self.stream.value_namespace = name_space
                self.stream.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-dependency"):
                self.subscription_dependency = value
                self.subscription_dependency.value_namespace = name_space
                self.subscription_dependency.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-priority"):
                self.subscription_priority = value
                self.subscription_priority.value_namespace = name_space
                self.subscription_priority.value_namespace_prefix = name_space_prefix
            if(value_path == "subtree-filter"):
                self.subtree_filter = value
                self.subtree_filter.value_namespace = name_space
                self.subtree_filter.value_namespace_prefix = name_space_prefix
            if(value_path == "xpath-filter"):
                self.xpath_filter = value
                self.xpath_filter.value_namespace = name_space
                self.xpath_filter.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.subscription:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.subscription:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-event-notifications:subscription-config" + path_buffer

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

        if (child_yang_name == "subscription"):
            for c in self.subscription:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = SubscriptionConfig.Subscription()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.subscription.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "subscription"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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
    	**type**\: list of    :py:class:`Subscription <ydk.models.ietf.ietf_event_notifications.Subscriptions.Subscription>`
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Subscriptions, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriptions"
        self.yang_parent_name = "ietf-event-notifications"

        self.subscription = YList(self)

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
                    super(Subscriptions, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Subscriptions, self).__setattr__(name, value)


    class Subscription(Entity):
        """
        Content of a subscription.
        Subscriptions can be created using a control channel
        or RPC, or be established through configuration.
        
        .. attribute:: subscription_id  <key>
        
        	Identifier of this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: anchor_time
        
        	Designates a timestamp from which the series of periodic push updates are computed. The next update will take place at the next period interval from the anchor time.  For example, for an anchor time at the top of a minute and a period interval of a minute, the next update will be sent at the top of the next minute
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: configured_subscription
        
        	The presence of this leaf indicates that the subscription originated from configuration, not through a control channel or RPC
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: dampening_period
        
        	Minimum amount of time that needs to have passed since the last time an update was provided
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: dscp
        
        	The push update's IP packet transport priority. This is made visible across network hops to receiver. The transport priority is shared for all receivers of a given subscription
        	**type**\:  int
        
        	**range:** 0..63
        
        	**default value**\: 0
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`Encodings <ydk.models.ietf.ietf_event_notifications.Encodings>`
        
        	**default value**\: encode-xml
        
        .. attribute:: excluded_change
        
        	Use to restrict which changes trigger an update. For example, if modify is excluded, only creation and deletion of objects is reported
        	**type**\:  list of   :py:class:`ChangeType <ydk.models.ietf.ietf_yang_push.ChangeType>`
        
        .. attribute:: filter
        
        	Filter per RFC 5277. Notification filter. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References filter which is associated with the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`filter_id <ydk.models.ietf.ietf_event_notifications.Filters.Filter>`
        
        .. attribute:: no_synch_on_start
        
        	This leaf acts as a flag that determines behavior at the start of the subscription.  When present, synchronization of state at the beginning of the subscription is outside the scope of the subscription. Only updates about changes that are observed from the start time, i.e. only push\-change\-update notifications are sent. When absent (default behavior), in order to facilitate a receiver's synchronization, a full update is sent when the subscription starts using a push\-update notification, just like in the case of a periodic subscription.  After that, push\-change\-update notifications only are sent unless the Publisher chooses to resynch the subscription again
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: period
        
        	Duration of time which should occur between periodic push updates.  Where the anchor of a start\-time is available, the push will include the objects and their values which exist at an exact multiple of timeticks aligning to this start\-time anchor
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: receivers
        
        	Set of receivers in a subscription
        	**type**\:   :py:class:`Receivers <ydk.models.ietf.ietf_event_notifications.Subscriptions.Subscription.Receivers>`
        
        .. attribute:: source_address
        
        	The source address for the notifications
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        	**mandatory**\: True
        
        
        ----
        .. attribute:: source_interface
        
        	References the interface for notifications
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        .. attribute:: source_vrf
        
        	Label of the vrf
        	**type**\:  int
        
        	**range:** 16..1048574
        
        .. attribute:: starttime
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If <startTime> is not present, this is not a replay subscription.  It is not valid to specify start times that are later than the current time.  If the <startTime> specified is earlier than the log can support, the replay will begin with the earliest available notification.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stoptime
        
        	Used with the optional replay feature to indicate the newest notifications of interest.  If <stopTime> is not present, the notifications will continue until the subscription is terminated.  Must be used with and be later than <startTime>.  Values of <stopTime> in the future are valid.  This parameter is of type dateTime and compliant to [RFC3339].  Implementations must support time zones
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`Stream <ydk.models.ietf.ietf_event_notifications.Stream>`
        
        .. attribute:: subscription_dependency
        
        	Provides the Subscription ID of a parent subscription without which this subscription should not exist. In other words, there is no reason to stream these objects if another subscription is missing
        	**type**\:  str
        
        .. attribute:: subscription_priority
        
        	Relative priority for a subscription.   Allows an underlying transport layer perform informed load balance allocations between various subscriptions
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: subscription_status
        
        	The status of the subscription
        	**type**\:   :py:class:`SubscriptionStreamStatus <ydk.models.ietf.ietf_event_notifications.SubscriptionStreamStatus>`
        
        .. attribute:: subtree_filter
        
        	Subtree\-filter used to specify the data nodes targeted for subscription within a subtree, or subtrees, of a conceptual YANG datastore.  Objects matching the filter criteria will traverse the filter. The syntax follows the subtree filter syntax specified in RFC 6241, section 6
        	**type**\:  anyxml
        
        .. attribute:: xpath_filter
        
        	Xpath defining the data items of interest
        	**type**\:  str
        
        

        """

        _prefix = 'notif-bis'
        _revision = '2016-10-27'

        def __init__(self):
            super(Subscriptions.Subscription, self).__init__()

            self.yang_name = "subscription"
            self.yang_parent_name = "subscriptions"

            self.subscription_id = YLeaf(YType.uint32, "subscription-id")

            self.anchor_time = YLeaf(YType.str, "ietf-yang-push:anchor-time")

            self.configured_subscription = YLeaf(YType.empty, "configured-subscription")

            self.dampening_period = YLeaf(YType.uint32, "ietf-yang-push:dampening-period")

            self.dscp = YLeaf(YType.uint8, "ietf-yang-push:dscp")

            self.encoding = YLeaf(YType.identityref, "encoding")

            self.excluded_change = YLeafList(YType.enumeration, "ietf-yang-push:excluded-change")

            self.filter = YLeaf(YType.str, "filter")

            self.filter_ref = YLeaf(YType.str, "filter-ref")

            self.no_synch_on_start = YLeaf(YType.empty, "ietf-yang-push:no-synch-on-start")

            self.period = YLeaf(YType.uint32, "ietf-yang-push:period")

            self.source_address = YLeaf(YType.str, "source-address")

            self.source_interface = YLeaf(YType.str, "source-interface")

            self.source_vrf = YLeaf(YType.uint32, "source-vrf")

            self.starttime = YLeaf(YType.str, "startTime")

            self.stoptime = YLeaf(YType.str, "stopTime")

            self.stream = YLeaf(YType.identityref, "stream")

            self.subscription_dependency = YLeaf(YType.str, "ietf-yang-push:subscription-dependency")

            self.subscription_priority = YLeaf(YType.uint8, "ietf-yang-push:subscription-priority")

            self.subscription_status = YLeaf(YType.identityref, "subscription-status")

            self.subtree_filter = YLeaf(YType.str, "ietf-yang-push:subtree-filter")

            self.xpath_filter = YLeaf(YType.str, "ietf-yang-push:xpath-filter")

            self.receivers = Subscriptions.Subscription.Receivers()
            self.receivers.parent = self
            self._children_name_map["receivers"] = "receivers"
            self._children_yang_names.add("receivers")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("subscription_id",
                            "anchor_time",
                            "configured_subscription",
                            "dampening_period",
                            "dscp",
                            "encoding",
                            "excluded_change",
                            "filter",
                            "filter_ref",
                            "no_synch_on_start",
                            "period",
                            "source_address",
                            "source_interface",
                            "source_vrf",
                            "starttime",
                            "stoptime",
                            "stream",
                            "subscription_dependency",
                            "subscription_priority",
                            "subscription_status",
                            "subtree_filter",
                            "xpath_filter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Subscriptions.Subscription, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Subscriptions.Subscription, self).__setattr__(name, value)


        class Receivers(Entity):
            """
            Set of receivers in a subscription.
            
            .. attribute:: receiver
            
            	A single host or multipoint address intended as a target for the notifications for a subscription
            	**type**\: list of    :py:class:`Receiver <ydk.models.ietf.ietf_event_notifications.Subscriptions.Subscription.Receivers.Receiver>`
            
            

            """

            _prefix = 'notif-bis'
            _revision = '2016-10-27'

            def __init__(self):
                super(Subscriptions.Subscription.Receivers, self).__init__()

                self.yang_name = "receivers"
                self.yang_parent_name = "subscription"

                self.receiver = YList(self)

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
                            super(Subscriptions.Subscription.Receivers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Subscriptions.Subscription.Receivers, self).__setattr__(name, value)


            class Receiver(Entity):
                """
                A single host or multipoint address intended as a target
                for the notifications for a subscription.
                
                .. attribute:: address  <key>
                
                	Specifies the address for the traffic to reach a remote host. One of the following must be specified\: an ipv4 address, an ipv6 address, or a host name
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                
                ----
                
                ----
                	**type**\:  str
                
                	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
                
                	**mandatory**\: True
                
                
                ----
                .. attribute:: port
                
                	This leaf specifies the port number to use for messages destined for a receiver
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**mandatory**\: True
                
                .. attribute:: protocol
                
                	This leaf specifies the transport protocol used to deliver messages destined for the receiver
                	**type**\:   :py:class:`Transport <ydk.models.ietf.ietf_event_notifications.Transport>`
                
                	**default value**\: netconf
                
                

                """

                _prefix = 'notif-bis'
                _revision = '2016-10-27'

                def __init__(self):
                    super(Subscriptions.Subscription.Receivers.Receiver, self).__init__()

                    self.yang_name = "receiver"
                    self.yang_parent_name = "receivers"

                    self.address = YLeaf(YType.str, "address")

                    self.port = YLeaf(YType.uint16, "port")

                    self.protocol = YLeaf(YType.identityref, "protocol")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address",
                                    "port",
                                    "protocol") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Subscriptions.Subscription.Receivers.Receiver, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Subscriptions.Subscription.Receivers.Receiver, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.port.is_set or
                        self.protocol.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.protocol.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "receiver" + "[address='" + self.address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "port" or name == "protocol"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol"):
                        self.protocol = value
                        self.protocol.value_namespace = name_space
                        self.protocol.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.receiver:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.receiver:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "receivers" + path_buffer

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

                if (child_yang_name == "receiver"):
                    for c in self.receiver:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Subscriptions.Subscription.Receivers.Receiver()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.receiver.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "receiver"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.subscription_id.is_set or
                self.anchor_time.is_set or
                self.configured_subscription.is_set or
                self.dampening_period.is_set or
                self.dscp.is_set or
                self.encoding.is_set or
                self.filter.is_set or
                self.filter_ref.is_set or
                self.no_synch_on_start.is_set or
                self.period.is_set or
                self.source_address.is_set or
                self.source_interface.is_set or
                self.source_vrf.is_set or
                self.starttime.is_set or
                self.stoptime.is_set or
                self.stream.is_set or
                self.subscription_dependency.is_set or
                self.subscription_priority.is_set or
                self.subscription_status.is_set or
                self.subtree_filter.is_set or
                self.xpath_filter.is_set or
                (self.receivers is not None and self.receivers.has_data()))

        def has_operation(self):
            for leaf in self.excluded_change.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.subscription_id.yfilter != YFilter.not_set or
                self.anchor_time.yfilter != YFilter.not_set or
                self.configured_subscription.yfilter != YFilter.not_set or
                self.dampening_period.yfilter != YFilter.not_set or
                self.dscp.yfilter != YFilter.not_set or
                self.encoding.yfilter != YFilter.not_set or
                self.excluded_change.yfilter != YFilter.not_set or
                self.filter.yfilter != YFilter.not_set or
                self.filter_ref.yfilter != YFilter.not_set or
                self.no_synch_on_start.yfilter != YFilter.not_set or
                self.period.yfilter != YFilter.not_set or
                self.source_address.yfilter != YFilter.not_set or
                self.source_interface.yfilter != YFilter.not_set or
                self.source_vrf.yfilter != YFilter.not_set or
                self.starttime.yfilter != YFilter.not_set or
                self.stoptime.yfilter != YFilter.not_set or
                self.stream.yfilter != YFilter.not_set or
                self.subscription_dependency.yfilter != YFilter.not_set or
                self.subscription_priority.yfilter != YFilter.not_set or
                self.subscription_status.yfilter != YFilter.not_set or
                self.subtree_filter.yfilter != YFilter.not_set or
                self.xpath_filter.yfilter != YFilter.not_set or
                (self.receivers is not None and self.receivers.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "subscription" + "[subscription-id='" + self.subscription_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-event-notifications:subscriptions/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_id.get_name_leafdata())
            if (self.anchor_time.is_set or self.anchor_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.anchor_time.get_name_leafdata())
            if (self.configured_subscription.is_set or self.configured_subscription.yfilter != YFilter.not_set):
                leaf_name_data.append(self.configured_subscription.get_name_leafdata())
            if (self.dampening_period.is_set or self.dampening_period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dampening_period.get_name_leafdata())
            if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                leaf_name_data.append(self.dscp.get_name_leafdata())
            if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.encoding.get_name_leafdata())
            if (self.filter.is_set or self.filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter.get_name_leafdata())
            if (self.filter_ref.is_set or self.filter_ref.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filter_ref.get_name_leafdata())
            if (self.no_synch_on_start.is_set or self.no_synch_on_start.yfilter != YFilter.not_set):
                leaf_name_data.append(self.no_synch_on_start.get_name_leafdata())
            if (self.period.is_set or self.period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.period.get_name_leafdata())
            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_address.get_name_leafdata())
            if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_interface.get_name_leafdata())
            if (self.source_vrf.is_set or self.source_vrf.yfilter != YFilter.not_set):
                leaf_name_data.append(self.source_vrf.get_name_leafdata())
            if (self.starttime.is_set or self.starttime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.starttime.get_name_leafdata())
            if (self.stoptime.is_set or self.stoptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stoptime.get_name_leafdata())
            if (self.stream.is_set or self.stream.yfilter != YFilter.not_set):
                leaf_name_data.append(self.stream.get_name_leafdata())
            if (self.subscription_dependency.is_set or self.subscription_dependency.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_dependency.get_name_leafdata())
            if (self.subscription_priority.is_set or self.subscription_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_priority.get_name_leafdata())
            if (self.subscription_status.is_set or self.subscription_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subscription_status.get_name_leafdata())
            if (self.subtree_filter.is_set or self.subtree_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.subtree_filter.get_name_leafdata())
            if (self.xpath_filter.is_set or self.xpath_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.xpath_filter.get_name_leafdata())

            leaf_name_data.extend(self.excluded_change.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "receivers"):
                if (self.receivers is None):
                    self.receivers = Subscriptions.Subscription.Receivers()
                    self.receivers.parent = self
                    self._children_name_map["receivers"] = "receivers"
                return self.receivers

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "receivers" or name == "subscription-id" or name == "anchor-time" or name == "configured-subscription" or name == "dampening-period" or name == "dscp" or name == "encoding" or name == "excluded-change" or name == "filter" or name == "filter-ref" or name == "no-synch-on-start" or name == "period" or name == "source-address" or name == "source-interface" or name == "source-vrf" or name == "startTime" or name == "stopTime" or name == "stream" or name == "subscription-dependency" or name == "subscription-priority" or name == "subscription-status" or name == "subtree-filter" or name == "xpath-filter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "subscription-id"):
                self.subscription_id = value
                self.subscription_id.value_namespace = name_space
                self.subscription_id.value_namespace_prefix = name_space_prefix
            if(value_path == "anchor-time"):
                self.anchor_time = value
                self.anchor_time.value_namespace = name_space
                self.anchor_time.value_namespace_prefix = name_space_prefix
            if(value_path == "configured-subscription"):
                self.configured_subscription = value
                self.configured_subscription.value_namespace = name_space
                self.configured_subscription.value_namespace_prefix = name_space_prefix
            if(value_path == "dampening-period"):
                self.dampening_period = value
                self.dampening_period.value_namespace = name_space
                self.dampening_period.value_namespace_prefix = name_space_prefix
            if(value_path == "dscp"):
                self.dscp = value
                self.dscp.value_namespace = name_space
                self.dscp.value_namespace_prefix = name_space_prefix
            if(value_path == "encoding"):
                self.encoding = value
                self.encoding.value_namespace = name_space
                self.encoding.value_namespace_prefix = name_space_prefix
            if(value_path == "excluded-change"):
                self.excluded_change.append(value)
            if(value_path == "filter"):
                self.filter = value
                self.filter.value_namespace = name_space
                self.filter.value_namespace_prefix = name_space_prefix
            if(value_path == "filter-ref"):
                self.filter_ref = value
                self.filter_ref.value_namespace = name_space
                self.filter_ref.value_namespace_prefix = name_space_prefix
            if(value_path == "no-synch-on-start"):
                self.no_synch_on_start = value
                self.no_synch_on_start.value_namespace = name_space
                self.no_synch_on_start.value_namespace_prefix = name_space_prefix
            if(value_path == "period"):
                self.period = value
                self.period.value_namespace = name_space
                self.period.value_namespace_prefix = name_space_prefix
            if(value_path == "source-address"):
                self.source_address = value
                self.source_address.value_namespace = name_space
                self.source_address.value_namespace_prefix = name_space_prefix
            if(value_path == "source-interface"):
                self.source_interface = value
                self.source_interface.value_namespace = name_space
                self.source_interface.value_namespace_prefix = name_space_prefix
            if(value_path == "source-vrf"):
                self.source_vrf = value
                self.source_vrf.value_namespace = name_space
                self.source_vrf.value_namespace_prefix = name_space_prefix
            if(value_path == "startTime"):
                self.starttime = value
                self.starttime.value_namespace = name_space
                self.starttime.value_namespace_prefix = name_space_prefix
            if(value_path == "stopTime"):
                self.stoptime = value
                self.stoptime.value_namespace = name_space
                self.stoptime.value_namespace_prefix = name_space_prefix
            if(value_path == "stream"):
                self.stream = value
                self.stream.value_namespace = name_space
                self.stream.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-dependency"):
                self.subscription_dependency = value
                self.subscription_dependency.value_namespace = name_space
                self.subscription_dependency.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-priority"):
                self.subscription_priority = value
                self.subscription_priority.value_namespace = name_space
                self.subscription_priority.value_namespace_prefix = name_space_prefix
            if(value_path == "subscription-status"):
                self.subscription_status = value
                self.subscription_status.value_namespace = name_space
                self.subscription_status.value_namespace_prefix = name_space_prefix
            if(value_path == "subtree-filter"):
                self.subtree_filter = value
                self.subtree_filter.value_namespace = name_space
                self.subtree_filter.value_namespace_prefix = name_space_prefix
            if(value_path == "xpath-filter"):
                self.xpath_filter = value
                self.xpath_filter.value_namespace = name_space
                self.xpath_filter.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.subscription:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.subscription:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ietf-event-notifications:subscriptions" + path_buffer

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

        if (child_yang_name == "subscription"):
            for c in self.subscription:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Subscriptions.Subscription()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.subscription.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "subscription"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Subscriptions()
        return self._top_entity

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


class Other(Identity):
    """
    Fallback reason \- any other reason
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Other, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:other")


class Active(Identity):
    """
    Status is active and healthy.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Active, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:active")


class EncodeJson(Identity):
    """
    Encode data using JSON
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(EncodeJson, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:encode-json")


class Error(Identity):
    """
    RPC was not successful.
    Base identity for error return codes.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Error, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error")


class InternalError(Identity):
    """
    Subscription failures caused by server internal error.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(InternalError, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:internal-error")


class EncodeXml(Identity):
    """
    Encode data using XML
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(EncodeXml, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:encode-xml")


class SubscriptionDeleted(Identity):
    """
    The subscription was terminated because the subscription
    was deleted.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(SubscriptionDeleted, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:subscription-deleted")


class ErrorNoSuchSubscription(Identity):
    """
    A subscription with the requested subscription ID
    does not exist.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ErrorNoSuchSubscription, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error-no-such-subscription")


class Ok(Identity):
    """
    OK \- RPC was successful and was performed as requested.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Ok, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:ok")


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


class Netconf(Identity):
    """
    Netconf notifications as a transport.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Netconf, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:netconf")


class Netconf(Identity):
    """
    Default NETCONF event stream, containing events based on
    notifications defined as YANG modules that are supported
    by the system.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Netconf, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:NETCONF")


class Inactive(Identity):
    """
    Status is inactive, for example outside the
    interval between start time and stop time.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(Inactive, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:inactive")


class NoResources(Identity):
    """
    Lack of resources, e.g. CPU, memory, bandwidth
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(NoResources, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:no-resources")


class ErrorInsufficientResources(Identity):
    """
    The publisher has insufficient resources to support the
    subscription as requested.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ErrorInsufficientResources, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error-insufficient-resources")


class ErrorNoSuchOption(Identity):
    """
    A requested parameter setting is not supported.
    
    

    """

    _prefix = 'notif-bis'
    _revision = '2016-10-27'

    def __init__(self):
        super(ErrorNoSuchOption, self).__init__("urn:ietf:params:xml:ns:yang:ietf-event-notifications", "ietf-event-notifications", "ietf-event-notifications:error-no-such-option")


