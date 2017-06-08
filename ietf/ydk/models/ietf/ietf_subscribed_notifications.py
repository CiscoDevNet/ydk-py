""" ietf_subscribed_notifications 

This module contains conceptual YANG specifications for NETCONF
Event Notifications.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class NotificationOriginEnum(Enum):
    """
    NotificationOriginEnum

    Specifies from where notifications will be sourced when

    being sent by the publisher.

    .. data:: interface_originated = 0

    	Notifications will be sent from a specific interface on a

    	publisher

    .. data:: address_originated = 1

    	Notifications will be sent from a specific address on a

    	publisher

    """

    interface_originated = 0

    address_originated = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['NotificationOriginEnum']



class StreamIdentity(object):
    """
    Base identity to represent a generic stream of event
    notifications.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['StreamIdentity']['meta_info']


class EncodingsIdentity(object):
    """
    Base identity to represent data encodings
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['EncodingsIdentity']['meta_info']


class TransportIdentity(object):
    """
    An identity that represents a transport protocol for event
    notifications
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['TransportIdentity']['meta_info']


class SubscriptionResultIdentity(object):
    """
    Base identity for RPC responses to requests surrounding
    management (e.g. creation, modification, deletion) of
    subscriptions.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['SubscriptionResultIdentity']['meta_info']


class SubscriptionStreamStatusIdentity(object):
    """
    Base identity for the status of subscriptions and datastreams.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['SubscriptionStreamStatusIdentity']['meta_info']


class EstablishSubscriptionRpc(object):
    """
    This RPC allows a subscriber to create (and possibly negotiate)
    a subscription on its own behalf.  If successful, the
    subscription remains in effect for the duration of the
    subscriber's association with the publisher, or until the
    subscription is terminated. In case an error (as indicated by
    subscription\-result) is returned, the subscription is not
    created.  In that case, the RPC output MAY include suggested
    parameter settings that would have a high likelihood of
    succeeding in a subsequent establish\-subscription request.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_subscribed_notifications.EstablishSubscriptionRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_subscribed_notifications.EstablishSubscriptionRpc.Output>`
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        self.input = EstablishSubscriptionRpc.Input()
        self.input.parent = self
        self.output = EstablishSubscriptionRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`EncodingsIdentity <ydk.models.ietf.ietf_subscribed_notifications.EncodingsIdentity>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter which excludes whole event\-notifications. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered  out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned  value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References an existing filter which is to be applied to the potential events of the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`identifier <ydk.models.ietf.ietf_subscribed_notifications.Filters.Filter>`
        
        .. attribute:: replay_start_time
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If replay\-start\-time is not present, this is not a replay subscription and event pushes should start immediately.  It is never valid to specify start times that are later than or equal to the current time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stop_time
        
        	Identifies a time after which notification events should not be sent.  If stop\-time is not present, the notifications will continue until the subscription is terminated.  If replay\-start\-time exists, stop\-time must for a subsequent time. If replay\-start\-time doesn't exist, stop\-time must for a future time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`StreamIdentity <ydk.models.ietf.ietf_subscribed_notifications.StreamIdentity>`
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.encoding = None
            self.filter = None
            self.filter_ref = None
            self.replay_start_time = None
            self.stop_time = None
            self.stream = None

        @property
        def _common_path(self):

            return '/ietf-subscribed-notifications:establish-subscription/ietf-subscribed-notifications:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.encoding is not None:
                return True

            if self.filter is not None:
                return True

            if self.filter_ref is not None:
                return True

            if self.replay_start_time is not None:
                return True

            if self.stop_time is not None:
                return True

            if self.stream is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['EstablishSubscriptionRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: filter_failure
        
        	Information describing where and/or why a provided filter was unsupportable for a subscription
        	**type**\:  str
        
        .. attribute:: identifier
        
        	Identifier used for this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        .. attribute:: replay_start_time_hint
        
        	If a replay has been requested, but the requested replay   time cannot be honored, this may provide a hint at an alternate time which may be supportable
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:   :py:class:`SubscriptionResultIdentity <ydk.models.ietf.ietf_subscribed_notifications.SubscriptionResultIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.filter_failure = None
            self.identifier = None
            self.replay_start_time_hint = None
            self.subscription_result = None

        @property
        def _common_path(self):

            return '/ietf-subscribed-notifications:establish-subscription/ietf-subscribed-notifications:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.filter_failure is not None:
                return True

            if self.identifier is not None:
                return True

            if self.replay_start_time_hint is not None:
                return True

            if self.subscription_result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['EstablishSubscriptionRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-subscribed-notifications:establish-subscription'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['EstablishSubscriptionRpc']['meta_info']


class ModifySubscriptionRpc(object):
    """
    This RPC allows a subscriber to modify a subscription that was
    previously created using establish\-subscription.  If successful,
    the changed subscription remains in effect for the duration of
    the subscriber's association with the publisher, or until the
    subscription is again modified or terminated.  In case an error
    is returned (as indicated by subscription\-result), the
    subscription is not modified and the original subscription
    parameters remain in effect.  In that case, the rpc error
    response MAY include suggested parameter hints that would have
    a high likelihood of succeeding in a subsequent
    modify\-subscription request.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_subscribed_notifications.ModifySubscriptionRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_subscribed_notifications.ModifySubscriptionRpc.Output>`
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        self.input = ModifySubscriptionRpc.Input()
        self.input.parent = self
        self.output = ModifySubscriptionRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: filter
        
        	Filter which excludes whole event\-notifications. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered  out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned  value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References an existing filter which is to be applied to the potential events of the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`identifier <ydk.models.ietf.ietf_subscribed_notifications.Filters.Filter>`
        
        .. attribute:: identifier
        
        	Identifier to use for this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stop_time
        
        	Identifies a time after which notification events should not be sent.  If stop\-time is not present, the notifications will continue until the subscription is terminated.  If replay\-start\-time exists, stop\-time must for a subsequent time. If replay\-start\-time doesn't exist, stop\-time must for a future time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.filter = None
            self.filter_ref = None
            self.identifier = None
            self.stop_time = None

        @property
        def _common_path(self):

            return '/ietf-subscribed-notifications:modify-subscription/ietf-subscribed-notifications:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.filter is not None:
                return True

            if self.filter_ref is not None:
                return True

            if self.identifier is not None:
                return True

            if self.stop_time is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['ModifySubscriptionRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: filter_failure
        
        	Information describing where and/or why a provided filter was unsupportable for a subscription
        	**type**\:  str
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:   :py:class:`SubscriptionResultIdentity <ydk.models.ietf.ietf_subscribed_notifications.SubscriptionResultIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.filter_failure = None
            self.subscription_result = None

        @property
        def _common_path(self):

            return '/ietf-subscribed-notifications:modify-subscription/ietf-subscribed-notifications:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.filter_failure is not None:
                return True

            if self.subscription_result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['ModifySubscriptionRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-subscribed-notifications:modify-subscription'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['ModifySubscriptionRpc']['meta_info']


class DeleteSubscriptionRpc(object):
    """
    This RPC allows a subscriber to delete a subscription that
    was previously created from by that same subscriber using the
    establish\-subscription RPC.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_subscribed_notifications.DeleteSubscriptionRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_subscribed_notifications.DeleteSubscriptionRpc.Output>`
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        self.input = DeleteSubscriptionRpc.Input()
        self.input.parent = self
        self.output = DeleteSubscriptionRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: identifier
        
        	Identifier of the subscription that is to be deleted. Only subscriptions that were created using establish\-subscription can be deleted via this RPC
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.identifier = None

        @property
        def _common_path(self):

            return '/ietf-subscribed-notifications:delete-subscription/ietf-subscribed-notifications:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.identifier is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['DeleteSubscriptionRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:   :py:class:`SubscriptionResultIdentity <ydk.models.ietf.ietf_subscribed_notifications.SubscriptionResultIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.subscription_result = None

        @property
        def _common_path(self):

            return '/ietf-subscribed-notifications:delete-subscription/ietf-subscribed-notifications:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.subscription_result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['DeleteSubscriptionRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-subscribed-notifications:delete-subscription'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['DeleteSubscriptionRpc']['meta_info']


class KillSubscriptionRpc(object):
    """
    This RPC allows an operator to delete a dynamic subscription
    without restrictions on the originating subscriber or underlying
    transport session.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_subscribed_notifications.KillSubscriptionRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_subscribed_notifications.KillSubscriptionRpc.Output>`
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        self.input = KillSubscriptionRpc.Input()
        self.input.parent = self
        self.output = KillSubscriptionRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: identifier
        
        	Identifier of the subscription that is to be deleted. Only  subscriptions that were created using establish\-subscription can be deleted via this RPC
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.identifier = None

        @property
        def _common_path(self):

            return '/ietf-subscribed-notifications:kill-subscription/ietf-subscribed-notifications:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.identifier is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['KillSubscriptionRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: subscription_result
        
        	Indicates whether subscription is operational, or if a problem was encountered
        	**type**\:   :py:class:`SubscriptionResultIdentity <ydk.models.ietf.ietf_subscribed_notifications.SubscriptionResultIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.subscription_result = None

        @property
        def _common_path(self):

            return '/ietf-subscribed-notifications:kill-subscription/ietf-subscribed-notifications:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if not self.is_config():
                return False
            if self.subscription_result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['KillSubscriptionRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-subscribed-notifications:kill-subscription'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['KillSubscriptionRpc']['meta_info']


class Streams(object):
    """
    This container contains a leaf list of built\-in
    streams that are provided by the system.
    
    .. attribute:: stream
    
    	Identifies the built\-in streams that are supported by the system.  Built\-in streams are associated with their own identities, each of which carries a special semantics. In case configurable custom streams are supported, as indicated by the custom\-stream identity, the configuration of those custom streams is provided separately
    	**type**\:  
    		list of  
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        self.stream = YLeafList()
        self.stream.parent = self
        self.stream.name = 'stream'

    @property
    def _common_path(self):

        return '/ietf-subscribed-notifications:streams'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.stream is not None:
            for child_ref in self.stream:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['Streams']['meta_info']


class Filters(object):
    """
    This container contains a list of configurable filters
    that can be applied to subscriptions.  This facilitates
    the reuse of complex filters once defined.
    
    .. attribute:: filter
    
    	A list of configurable filters that can be applied to subscriptions
    	**type**\: list of    :py:class:`Filter <ydk.models.ietf.ietf_subscribed_notifications.Filters.Filter>`
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        self.filter = YList()
        self.filter.parent = self
        self.filter.name = 'filter'


    class Filter(object):
        """
        A list of configurable filters that can be applied to
        subscriptions.
        
        .. attribute:: identifier  <key>
        
        	An identifier to differentiate between filters
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: filter
        
        	Filter which excludes whole event\-notifications. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered  out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned  value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References an existing filter which is to be applied to the potential events of the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`identifier <ydk.models.ietf.ietf_subscribed_notifications.Filters.Filter>`
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.identifier = None
            self.filter = None
            self.filter_ref = None

        @property
        def _common_path(self):
            if self.identifier is None:
                raise YPYModelError('Key property identifier is None')

            return '/ietf-subscribed-notifications:filters/ietf-subscribed-notifications:filter[ietf-subscribed-notifications:identifier = ' + str(self.identifier) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.identifier is not None:
                return True

            if self.filter is not None:
                return True

            if self.filter_ref is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['Filters.Filter']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-subscribed-notifications:filters'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.filter is not None:
            for child_ref in self.filter:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['Filters']['meta_info']


class SubscriptionConfig(object):
    """
    Contains the list of subscriptions that are configured,
    as opposed to established via RPC or other means.
    
    .. attribute:: subscription
    
    	Content of a subscription
    	**type**\: list of    :py:class:`Subscription <ydk.models.ietf.ietf_subscribed_notifications.SubscriptionConfig.Subscription>`
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        self.subscription = YList()
        self.subscription.parent = self
        self.subscription.name = 'subscription'


    class Subscription(object):
        """
        Content of a subscription.
        
        .. attribute:: identifier  <key>
        
        	Identifier to use for this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`EncodingsIdentity <ydk.models.ietf.ietf_subscribed_notifications.EncodingsIdentity>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter which excludes whole event\-notifications. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered  out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned  value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References an existing filter which is to be applied to the potential events of the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`identifier <ydk.models.ietf.ietf_subscribed_notifications.Filters.Filter>`
        
        .. attribute:: receivers
        
        	Set of receivers in a subscription
        	**type**\:   :py:class:`Receivers <ydk.models.ietf.ietf_subscribed_notifications.SubscriptionConfig.Subscription.Receivers>`
        
        .. attribute:: source_address
        
        	The source address for the notifications
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: source_interface
        
        	References the interface for notifications
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        .. attribute:: source_vrf
        
        	Network instance name for the VRF.  This could also have been a leafref to draft\-ietf\-rtgwg\-ni\-model, but that model in not complete, and may not be implemented on a box
        	**type**\:  str
        
        .. attribute:: stop_time
        
        	Identifies a time after which notification events should not be sent.  If stop\-time is not present, the notifications will continue until the subscription is terminated.  If replay\-start\-time exists, stop\-time must for a subsequent time. If replay\-start\-time doesn't exist, stop\-time must for a future time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`StreamIdentity <ydk.models.ietf.ietf_subscribed_notifications.StreamIdentity>`
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.identifier = None
            self.encoding = None
            self.filter = None
            self.filter_ref = None
            self.receivers = SubscriptionConfig.Subscription.Receivers()
            self.receivers.parent = self
            self.source_address = None
            self.source_interface = None
            self.source_vrf = None
            self.stop_time = None
            self.stream = None


        class Receivers(object):
            """
            Set of receivers in a subscription.
            
            .. attribute:: receiver
            
            	A single host or multipoint address intended as a target for the notifications for a subscription
            	**type**\: list of    :py:class:`Receiver <ydk.models.ietf.ietf_subscribed_notifications.SubscriptionConfig.Subscription.Receivers.Receiver>`
            
            

            """

            _prefix = 'sn'
            _revision = '2017-02-23'

            def __init__(self):
                self.parent = None
                self.receiver = YList()
                self.receiver.parent = self
                self.receiver.name = 'receiver'


            class Receiver(object):
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
                .. attribute:: port  <key>
                
                	This leaf specifies the port number to use for messages destined for a receiver
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**mandatory**\: True
                
                .. attribute:: protocol
                
                	This leaf specifies the transport protocol used to deliver messages destined for the receiver.  Each protocol may use the address and port information differently as applicable
                	**type**\:   :py:class:`TransportIdentity <ydk.models.ietf.ietf_subscribed_notifications.TransportIdentity>`
                
                	**default value**\: netconf
                
                

                """

                _prefix = 'sn'
                _revision = '2017-02-23'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.port = None
                    self.protocol = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.address is None:
                        raise YPYModelError('Key property address is None')
                    if self.port is None:
                        raise YPYModelError('Key property port is None')

                    return self.parent._common_path +'/ietf-subscribed-notifications:receiver[ietf-subscribed-notifications:address = ' + str(self.address) + '][ietf-subscribed-notifications:port = ' + str(self.port) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None:
                        return True

                    if self.port is not None:
                        return True

                    if self.protocol is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
                    return meta._meta_table['SubscriptionConfig.Subscription.Receivers.Receiver']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-subscribed-notifications:receivers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.receiver is not None:
                    for child_ref in self.receiver:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
                return meta._meta_table['SubscriptionConfig.Subscription.Receivers']['meta_info']

        @property
        def _common_path(self):
            if self.identifier is None:
                raise YPYModelError('Key property identifier is None')

            return '/ietf-subscribed-notifications:subscription-config/ietf-subscribed-notifications:subscription[ietf-subscribed-notifications:identifier = ' + str(self.identifier) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.identifier is not None:
                return True

            if self.encoding is not None:
                return True

            if self.filter is not None:
                return True

            if self.filter_ref is not None:
                return True

            if self.receivers is not None and self.receivers._has_data():
                return True

            if self.source_address is not None:
                return True

            if self.source_interface is not None:
                return True

            if self.source_vrf is not None:
                return True

            if self.stop_time is not None:
                return True

            if self.stream is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['SubscriptionConfig.Subscription']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-subscribed-notifications:subscription-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.subscription is not None:
            for child_ref in self.subscription:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['SubscriptionConfig']['meta_info']


class Subscriptions(object):
    """
    Contains the list of currently active subscriptions, i.e.
    subscriptions that are currently in effect, used for subscription
    management and monitoring purposes. This includes subscriptions
    that have been setup via RPC primitives as well as subscriptions
    that have been established via configuration.
    
    .. attribute:: subscription
    
    	Content of a subscription. Subscriptions can be created using a control channel or RPC, or be established through configuration
    	**type**\: list of    :py:class:`Subscription <ydk.models.ietf.ietf_subscribed_notifications.Subscriptions.Subscription>`
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        self.subscription = YList()
        self.subscription.parent = self
        self.subscription.name = 'subscription'


    class Subscription(object):
        """
        Content of a subscription.
        Subscriptions can be created using a control channel or RPC, or
        be established through configuration.
        
        .. attribute:: identifier  <key>
        
        	Identifier of this subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: configured_subscription
        
        	The presence of this leaf indicates that the subscription originated from configuration, not through a control channel or RPC
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: encoding
        
        	The type of encoding for the subscribed data. Default is XML
        	**type**\:   :py:class:`EncodingsIdentity <ydk.models.ietf.ietf_subscribed_notifications.EncodingsIdentity>`
        
        	**default value**\: encode-xml
        
        .. attribute:: filter
        
        	Filter which excludes whole event\-notifications. If a filter element is specified to look for data of a particular value, and the data item is not present within a particular event notification for its value to be checked against, the notification will be filtered  out. For example, if one were to check for 'severity=critical' in a configuration event notification where this field was not supported, then the notification would be filtered out. For subtree filtering, a non\-empty node set means that the filter matches.  For XPath filtering, the mechanisms defined in [XPATH] should be used to convert the returned  value to boolean
        	**type**\:  anyxml
        
        .. attribute:: filter_ref
        
        	References an existing filter which is to be applied to the potential events of the subscription
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**refers to**\:  :py:class:`identifier <ydk.models.ietf.ietf_subscribed_notifications.Filters.Filter>`
        
        .. attribute:: receivers
        
        	Set of receivers in a subscription
        	**type**\:   :py:class:`Receivers <ydk.models.ietf.ietf_subscribed_notifications.Subscriptions.Subscription.Receivers>`
        
        .. attribute:: replay_start_time
        
        	Used to trigger the replay feature and indicate that the replay should start at the time specified.  If replay\-start\-time is not present, this is not a replay subscription and event pushes should start immediately.  It is never valid to specify start times that are later than or equal to the current time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: source_address
        
        	The source address for the notifications
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: source_interface
        
        	References the interface for notifications
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        .. attribute:: source_vrf
        
        	Network instance name for the VRF.  This could also have been a leafref to draft\-ietf\-rtgwg\-ni\-model, but that model in not complete, and may not be implemented on a box
        	**type**\:  str
        
        .. attribute:: stop_time
        
        	Identifies a time after which notification events should not be sent.  If stop\-time is not present, the notifications will continue until the subscription is terminated.  If replay\-start\-time exists, stop\-time must for a subsequent time. If replay\-start\-time doesn't exist, stop\-time must for a future time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: stream
        
        	Indicates which stream of events is of interest. If not present, events in the default NETCONF stream will be sent
        	**type**\:   :py:class:`StreamIdentity <ydk.models.ietf.ietf_subscribed_notifications.StreamIdentity>`
        
        .. attribute:: subscription_status
        
        	The status of the subscription
        	**type**\:   :py:class:`SubscriptionStreamStatusIdentity <ydk.models.ietf.ietf_subscribed_notifications.SubscriptionStreamStatusIdentity>`
        
        

        """

        _prefix = 'sn'
        _revision = '2017-02-23'

        def __init__(self):
            self.parent = None
            self.identifier = None
            self.configured_subscription = None
            self.encoding = None
            self.filter = None
            self.filter_ref = None
            self.receivers = Subscriptions.Subscription.Receivers()
            self.receivers.parent = self
            self.replay_start_time = None
            self.source_address = None
            self.source_interface = None
            self.source_vrf = None
            self.stop_time = None
            self.stream = None
            self.subscription_status = None


        class Receivers(object):
            """
            Set of receivers in a subscription.
            
            .. attribute:: receiver
            
            	A single host or multipoint address intended as a target for the notifications for a subscription
            	**type**\: list of    :py:class:`Receiver <ydk.models.ietf.ietf_subscribed_notifications.Subscriptions.Subscription.Receivers.Receiver>`
            
            

            """

            _prefix = 'sn'
            _revision = '2017-02-23'

            def __init__(self):
                self.parent = None
                self.receiver = YList()
                self.receiver.parent = self
                self.receiver.name = 'receiver'


            class Receiver(object):
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
                .. attribute:: port  <key>
                
                	This leaf specifies the port number to use for messages destined for a receiver
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**mandatory**\: True
                
                .. attribute:: excluded_notifications
                
                	Operational data which provides the number of non\- datastore update notifications explicitly removed via filtering so that they are not sent to a receiver
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: protocol
                
                	This leaf specifies the transport protocol used to deliver messages destined for the receiver.  Each protocol may use the address and port information differently as applicable
                	**type**\:   :py:class:`TransportIdentity <ydk.models.ietf.ietf_subscribed_notifications.TransportIdentity>`
                
                	**default value**\: netconf
                
                .. attribute:: pushed_notifications
                
                	Operational data which provides the number of update notifications pushed to a receiver
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'sn'
                _revision = '2017-02-23'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.port = None
                    self.excluded_notifications = None
                    self.protocol = None
                    self.pushed_notifications = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.address is None:
                        raise YPYModelError('Key property address is None')
                    if self.port is None:
                        raise YPYModelError('Key property port is None')

                    return self.parent._common_path +'/ietf-subscribed-notifications:receiver[ietf-subscribed-notifications:address = ' + str(self.address) + '][ietf-subscribed-notifications:port = ' + str(self.port) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None:
                        return True

                    if self.port is not None:
                        return True

                    if self.excluded_notifications is not None:
                        return True

                    if self.protocol is not None:
                        return True

                    if self.pushed_notifications is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
                    return meta._meta_table['Subscriptions.Subscription.Receivers.Receiver']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-subscribed-notifications:receivers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.receiver is not None:
                    for child_ref in self.receiver:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
                return meta._meta_table['Subscriptions.Subscription.Receivers']['meta_info']

        @property
        def _common_path(self):
            if self.identifier is None:
                raise YPYModelError('Key property identifier is None')

            return '/ietf-subscribed-notifications:subscriptions/ietf-subscribed-notifications:subscription[ietf-subscribed-notifications:identifier = ' + str(self.identifier) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.identifier is not None:
                return True

            if self.configured_subscription is not None:
                return True

            if self.encoding is not None:
                return True

            if self.filter is not None:
                return True

            if self.filter_ref is not None:
                return True

            if self.receivers is not None and self.receivers._has_data():
                return True

            if self.replay_start_time is not None:
                return True

            if self.source_address is not None:
                return True

            if self.source_interface is not None:
                return True

            if self.source_vrf is not None:
                return True

            if self.stop_time is not None:
                return True

            if self.stream is not None:
                return True

            if self.subscription_status is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
            return meta._meta_table['Subscriptions.Subscription']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-subscribed-notifications:subscriptions'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.subscription is not None:
            for child_ref in self.subscription:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['Subscriptions']['meta_info']


class SuspendedIdentity(SubscriptionStreamStatusIdentity):
    """
    The status is suspended, meaning that the publisher is currently
    unable to provide the negotiated updates for the subscription.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        SubscriptionStreamStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['SuspendedIdentity']['meta_info']


class EncodeJsonIdentity(EncodingsIdentity):
    """
    Encode data using JSON
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        EncodingsIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['EncodeJsonIdentity']['meta_info']


class InErrorIdentity(SubscriptionStreamStatusIdentity):
    """
    The status is in error or degraded, meaning that stream and/or
    subscription is currently unable to provide the negotiated
    notifications.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        SubscriptionStreamStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['InErrorIdentity']['meta_info']


class NetconfIdentity(TransportIdentity):
    """
    Netconf notifications as a transport.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        TransportIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['NetconfIdentity']['meta_info']


class ErrorIdentity(SubscriptionResultIdentity):
    """
    RPC was not successful.
    Base identity for error return codes.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        SubscriptionResultIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['ErrorIdentity']['meta_info']


class ActiveIdentity(SubscriptionStreamStatusIdentity):
    """
    Status is active and healthy.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        SubscriptionStreamStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['ActiveIdentity']['meta_info']


class HistoryUnavailableIdentity(ErrorIdentity):
    """
    Replay request too far into the past. The publisher does store
    historic information for all parts of requested subscription, but
    not back to the requested timestamp.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['HistoryUnavailableIdentity']['meta_info']


class NamespaceUnavailableIdentity(ErrorIdentity):
    """
    Referenced namespace doesn't exist or is unavailable
    to the receiver.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['NamespaceUnavailableIdentity']['meta_info']


class NetconfIdentity(StreamIdentity):
    """
    Default NETCONF event stream, containing events based on
    notifications defined as YANG modules that are supported by the
    system.  This contains the same set of events in a default
    RFC\-5277 NETCONF stream
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        StreamIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['NetconfIdentity']['meta_info']


class OkIdentity(SubscriptionResultIdentity):
    """
    OK \- RPC was successful and was performed as requested.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        SubscriptionResultIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['OkIdentity']['meta_info']


class EncodeXmlIdentity(EncodingsIdentity):
    """
    Encode data using XML
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        EncodingsIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['EncodeXmlIdentity']['meta_info']


class SuspensionTimeoutIdentity(ErrorIdentity):
    """
    Termination of previously suspended subscription. The publisher
    has eliminated the subscription as it exceeded a time limit for
    suspension.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['SuspensionTimeoutIdentity']['meta_info']


class InactiveIdentity(SubscriptionStreamStatusIdentity):
    """
    Status is inactive, for example outside the interval between
    start time and stop time.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        SubscriptionStreamStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['InactiveIdentity']['meta_info']


class NoSuchSubscriptionIdentity(ErrorIdentity):
    """
    Referenced subscription doesn't exist. This may be as a result of
    a non\-existent subscription ID, an ID which belongs to another
    subscriber, or an ID for acceptable subscription which has been
    statically configured.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['NoSuchSubscriptionIdentity']['meta_info']


class EncodingUnavailableIdentity(ErrorIdentity):
    """
    Encoding not supported
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['EncodingUnavailableIdentity']['meta_info']


class ReplayUnsupportedIdentity(ErrorIdentity):
    """
    Replay cannot be performed for this subscription. The publisher
    does not provide the requested historic information via replay.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['ReplayUnsupportedIdentity']['meta_info']


class StreamUnavailableIdentity(ErrorIdentity):
    """
    Stream name does not exist or is not available to the receiver.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['StreamUnavailableIdentity']['meta_info']


class InternalErrorIdentity(ErrorIdentity):
    """
    Error within publisher prohibits operation.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['InternalErrorIdentity']['meta_info']


class FilterUnavailableIdentity(ErrorIdentity):
    """
    Referenced filter does not exist
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['FilterUnavailableIdentity']['meta_info']


class FilterUnsupportedIdentity(ErrorIdentity):
    """
    Cannot parse syntax within the filter. Failure can be from a
    syntax error, or a syntax too complex to be processed by the
    platform. The supplemental info should include the invalid part
    of the filter.
    
    

    """

    _prefix = 'sn'
    _revision = '2017-02-23'

    def __init__(self):
        ErrorIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_subscribed_notifications as meta
        return meta._meta_table['FilterUnsupportedIdentity']['meta_info']


