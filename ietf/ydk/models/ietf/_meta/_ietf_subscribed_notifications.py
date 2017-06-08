


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'NotificationOriginEnum' : _MetaInfoEnum('NotificationOriginEnum', 'ydk.models.ietf.ietf_subscribed_notifications',
        {
            'interface-originated':'interface_originated',
            'address-originated':'address_originated',
        }, 'ietf-subscribed-notifications', _yang_ns._namespaces['ietf-subscribed-notifications']),
    'StreamIdentity' : {
        'meta_info' : _MetaInfoClass('StreamIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'stream',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'EncodingsIdentity' : {
        'meta_info' : _MetaInfoClass('EncodingsIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'encodings',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'TransportIdentity' : {
        'meta_info' : _MetaInfoClass('TransportIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'transport',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'SubscriptionResultIdentity' : {
        'meta_info' : _MetaInfoClass('SubscriptionResultIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'subscription-result',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'SubscriptionStreamStatusIdentity' : {
        'meta_info' : _MetaInfoClass('SubscriptionStreamStatusIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'subscription-stream-status',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'EstablishSubscriptionRpc.Input' : {
        'meta_info' : _MetaInfoClass('EstablishSubscriptionRpc.Input',
            False, 
            [
            _MetaInfoClassMember('stream', REFERENCE_IDENTITY_CLASS, 'StreamIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'StreamIdentity', 
                [], [], 
                '''                Indicates which stream of events is of interest.
                If not present, events in the default NETCONF stream
                will be sent.
                ''',
                'stream',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('encoding', REFERENCE_IDENTITY_CLASS, 'EncodingsIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'EncodingsIdentity', 
                [], [], 
                '''                The type of encoding for the subscribed data.
                Default is XML
                ''',
                'encoding',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('replay-start-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Used to trigger the replay feature and indicate that the
                replay should start at the time specified.  If replay-start-time
                is not present, this is not a replay subscription and event
                pushes should start immediately.  It is never valid to
                specify start times that are later than or equal to the
                current time.
                ''',
                'replay_start_time',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('stop-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Identifies a time after which notification events should not
                be sent.  If stop-time is not present, the notifications will
                continue until the subscription is terminated.  If
                replay-start-time exists, stop-time must for a subsequent time.
                If replay-start-time doesn't exist, stop-time must for a future
                time.
                ''',
                'stop_time',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                References an existing filter which is to be applied to
                the potential events of the subscription.
                ''',
                'filter_ref',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Filter which excludes whole event-notifications. If a filter
                element is specified to look for data of a particular
                value, and the data item is not present within a particular
                event notification for its value to be checked against, the
                notification will be filtered  out. For example, if one
                were to check for 'severity=critical' in a configuration
                event notification where this field was not supported, then
                the notification would be filtered out. For subtree
                filtering, a non-empty node set means that the filter
                matches.  For XPath filtering, the mechanisms defined in
                [XPATH] should be used to convert the returned  value to
                boolean.
                ''',
                'filter',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'input',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'EstablishSubscriptionRpc.Output' : {
        'meta_info' : _MetaInfoClass('EstablishSubscriptionRpc.Output',
            False, 
            [
            _MetaInfoClassMember('subscription-result', REFERENCE_IDENTITY_CLASS, 'SubscriptionResultIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'SubscriptionResultIdentity', 
                [], [], 
                '''                Indicates whether subscription is operational, or if a problem
                was encountered.
                ''',
                'subscription_result',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter-failure', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Information describing where and/or why a provided filter was
                unsupportable for a subscription.
                ''',
                'filter_failure',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('replay-start-time-hint', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                If a replay has been requested, but the requested replay
                  time cannot be honored, this may provide a hint at an
                alternate time which may be supportable.
                ''',
                'replay_start_time_hint',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier used for this subscription.
                ''',
                'identifier',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'output',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'EstablishSubscriptionRpc' : {
        'meta_info' : _MetaInfoClass('EstablishSubscriptionRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_subscribed_notifications', 'EstablishSubscriptionRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_subscribed_notifications', 'EstablishSubscriptionRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'establish-subscription',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'ModifySubscriptionRpc.Input' : {
        'meta_info' : _MetaInfoClass('ModifySubscriptionRpc.Input',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier to use for this subscription.
                ''',
                'identifier',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('stop-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Identifies a time after which notification events should not
                be sent.  If stop-time is not present, the notifications will
                continue until the subscription is terminated.  If
                replay-start-time exists, stop-time must for a subsequent time.
                If replay-start-time doesn't exist, stop-time must for a future
                time.
                ''',
                'stop_time',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                References an existing filter which is to be applied to
                the potential events of the subscription.
                ''',
                'filter_ref',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Filter which excludes whole event-notifications. If a filter
                element is specified to look for data of a particular
                value, and the data item is not present within a particular
                event notification for its value to be checked against, the
                notification will be filtered  out. For example, if one
                were to check for 'severity=critical' in a configuration
                event notification where this field was not supported, then
                the notification would be filtered out. For subtree
                filtering, a non-empty node set means that the filter
                matches.  For XPath filtering, the mechanisms defined in
                [XPATH] should be used to convert the returned  value to
                boolean.
                ''',
                'filter',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'input',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'ModifySubscriptionRpc.Output' : {
        'meta_info' : _MetaInfoClass('ModifySubscriptionRpc.Output',
            False, 
            [
            _MetaInfoClassMember('subscription-result', REFERENCE_IDENTITY_CLASS, 'SubscriptionResultIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'SubscriptionResultIdentity', 
                [], [], 
                '''                Indicates whether subscription is operational, or if a problem
                was encountered.
                ''',
                'subscription_result',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter-failure', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Information describing where and/or why a provided filter was
                unsupportable for a subscription.
                ''',
                'filter_failure',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'output',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'ModifySubscriptionRpc' : {
        'meta_info' : _MetaInfoClass('ModifySubscriptionRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_subscribed_notifications', 'ModifySubscriptionRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_subscribed_notifications', 'ModifySubscriptionRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'modify-subscription',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'DeleteSubscriptionRpc.Input' : {
        'meta_info' : _MetaInfoClass('DeleteSubscriptionRpc.Input',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier of the subscription that is to be deleted.
                Only subscriptions that were created using
                establish-subscription can be deleted via this RPC.
                ''',
                'identifier',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'input',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'DeleteSubscriptionRpc.Output' : {
        'meta_info' : _MetaInfoClass('DeleteSubscriptionRpc.Output',
            False, 
            [
            _MetaInfoClassMember('subscription-result', REFERENCE_IDENTITY_CLASS, 'SubscriptionResultIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'SubscriptionResultIdentity', 
                [], [], 
                '''                Indicates whether subscription is operational, or if a
                problem was encountered.
                ''',
                'subscription_result',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'output',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'DeleteSubscriptionRpc' : {
        'meta_info' : _MetaInfoClass('DeleteSubscriptionRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_subscribed_notifications', 'DeleteSubscriptionRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_subscribed_notifications', 'DeleteSubscriptionRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'delete-subscription',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'KillSubscriptionRpc.Input' : {
        'meta_info' : _MetaInfoClass('KillSubscriptionRpc.Input',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier of the subscription that is to be deleted. Only
                 subscriptions that were created using establish-subscription
                can be deleted via this RPC.
                ''',
                'identifier',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'input',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'KillSubscriptionRpc.Output' : {
        'meta_info' : _MetaInfoClass('KillSubscriptionRpc.Output',
            False, 
            [
            _MetaInfoClassMember('subscription-result', REFERENCE_IDENTITY_CLASS, 'SubscriptionResultIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'SubscriptionResultIdentity', 
                [], [], 
                '''                Indicates whether subscription is operational, or if a
                problem was encountered.
                ''',
                'subscription_result',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'output',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'KillSubscriptionRpc' : {
        'meta_info' : _MetaInfoClass('KillSubscriptionRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_subscribed_notifications', 'KillSubscriptionRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_subscribed_notifications', 'KillSubscriptionRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'kill-subscription',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'Streams' : {
        'meta_info' : _MetaInfoClass('Streams',
            False, 
            [
            _MetaInfoClassMember('stream', REFERENCE_LEAFLIST, 'StreamIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'StreamIdentity', 
                [], [], 
                '''                Identifies the built-in streams that are supported by the
                system.  Built-in streams are associated with their own
                identities, each of which carries a special semantics.
                In case configurable custom streams are supported,
                as indicated by the custom-stream identity, the configuration
                of those custom streams is provided separately.
                ''',
                'stream',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'streams',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'Filters.Filter' : {
        'meta_info' : _MetaInfoClass('Filters.Filter',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier to differentiate between filters.
                ''',
                'identifier',
                'ietf-subscribed-notifications', True),
            _MetaInfoClassMember('filter-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                References an existing filter which is to be applied to
                the potential events of the subscription.
                ''',
                'filter_ref',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Filter which excludes whole event-notifications. If a filter
                element is specified to look for data of a particular
                value, and the data item is not present within a particular
                event notification for its value to be checked against, the
                notification will be filtered  out. For example, if one
                were to check for 'severity=critical' in a configuration
                event notification where this field was not supported, then
                the notification would be filtered out. For subtree
                filtering, a non-empty node set means that the filter
                matches.  For XPath filtering, the mechanisms defined in
                [XPATH] should be used to convert the returned  value to
                boolean.
                ''',
                'filter',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'filter',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'Filters' : {
        'meta_info' : _MetaInfoClass('Filters',
            False, 
            [
            _MetaInfoClassMember('filter', REFERENCE_LIST, 'Filter' , 'ydk.models.ietf.ietf_subscribed_notifications', 'Filters.Filter', 
                [], [], 
                '''                A list of configurable filters that can be applied to
                subscriptions.
                ''',
                'filter',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'filters',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'SubscriptionConfig.Subscription.Receivers.Receiver' : {
        'meta_info' : _MetaInfoClass('SubscriptionConfig.Subscription.Receivers.Receiver',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specifies the address for the traffic to reach a remote
                host. One of the following must be specified: an ipv4
                address, an ipv6 address, or a host name.
                ''',
                'address',
                'ietf-subscribed-notifications', True, [
                    _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Specifies the address for the traffic to reach a remote
                        host. One of the following must be specified: an ipv4
                        address, an ipv6 address, or a host name.
                        ''',
                        'address',
                        'ietf-subscribed-notifications', True, [
                            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Specifies the address for the traffic to reach a remote
                                host. One of the following must be specified: an ipv4
                                address, an ipv6 address, or a host name.
                                ''',
                                'address',
                                'ietf-subscribed-notifications', True),
                            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Specifies the address for the traffic to reach a remote
                                host. One of the following must be specified: an ipv4
                                address, an ipv6 address, or a host name.
                                ''',
                                'address',
                                'ietf-subscribed-notifications', True),
                        ]),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                        '''                        Specifies the address for the traffic to reach a remote
                        host. One of the following must be specified: an ipv4
                        address, an ipv6 address, or a host name.
                        ''',
                        'address',
                        'ietf-subscribed-notifications', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This leaf specifies the port number to use for messages
                destined for a receiver.
                ''',
                'port',
                'ietf-subscribed-notifications', True),
            _MetaInfoClassMember('protocol', REFERENCE_IDENTITY_CLASS, 'TransportIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'TransportIdentity', 
                [], [], 
                '''                This leaf specifies the transport protocol used
                to deliver messages destined for the receiver.  Each
                protocol may use the address and port information
                differently as applicable.
                ''',
                'protocol',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'receiver',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'SubscriptionConfig.Subscription.Receivers' : {
        'meta_info' : _MetaInfoClass('SubscriptionConfig.Subscription.Receivers',
            False, 
            [
            _MetaInfoClassMember('receiver', REFERENCE_LIST, 'Receiver' , 'ydk.models.ietf.ietf_subscribed_notifications', 'SubscriptionConfig.Subscription.Receivers.Receiver', 
                [], [], 
                '''                A single host or multipoint address intended as a target
                for the notifications for a subscription.
                ''',
                'receiver',
                'ietf-subscribed-notifications', False, min_elements=1),
            ],
            'ietf-subscribed-notifications',
            'receivers',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'SubscriptionConfig.Subscription' : {
        'meta_info' : _MetaInfoClass('SubscriptionConfig.Subscription',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier to use for this subscription.
                ''',
                'identifier',
                'ietf-subscribed-notifications', True),
            _MetaInfoClassMember('stream', REFERENCE_IDENTITY_CLASS, 'StreamIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'StreamIdentity', 
                [], [], 
                '''                Indicates which stream of events is of interest.
                If not present, events in the default NETCONF stream
                will be sent.
                ''',
                'stream',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('encoding', REFERENCE_IDENTITY_CLASS, 'EncodingsIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'EncodingsIdentity', 
                [], [], 
                '''                The type of encoding for the subscribed data.
                Default is XML
                ''',
                'encoding',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('stop-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Identifies a time after which notification events should not
                be sent.  If stop-time is not present, the notifications will
                continue until the subscription is terminated.  If
                replay-start-time exists, stop-time must for a subsequent time.
                If replay-start-time doesn't exist, stop-time must for a future
                time.
                ''',
                'stop_time',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                References an existing filter which is to be applied to
                the potential events of the subscription.
                ''',
                'filter_ref',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Filter which excludes whole event-notifications. If a filter
                element is specified to look for data of a particular
                value, and the data item is not present within a particular
                event notification for its value to be checked against, the
                notification will be filtered  out. For example, if one
                were to check for 'severity=critical' in a configuration
                event notification where this field was not supported, then
                the notification would be filtered out. For subtree
                filtering, a non-empty node set means that the filter
                matches.  For XPath filtering, the mechanisms defined in
                [XPATH] should be used to convert the returned  value to
                boolean.
                ''',
                'filter',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('receivers', REFERENCE_CLASS, 'Receivers' , 'ydk.models.ietf.ietf_subscribed_notifications', 'SubscriptionConfig.Subscription.Receivers', 
                [], [], 
                '''                Set of receivers in a subscription.
                ''',
                'receivers',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References the interface for notifications.
                ''',
                'source_interface',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('source-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Network instance name for the VRF.  This could also have
                been a leafref to draft-ietf-rtgwg-ni-model, but that model
                in not complete, and may not be implemented on a box.
                ''',
                'source_vrf',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The source address for the notifications.
                ''',
                'source_address',
                'ietf-subscribed-notifications', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The source address for the notifications.
                        ''',
                        'source_address',
                        'ietf-subscribed-notifications', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The source address for the notifications.
                        ''',
                        'source_address',
                        'ietf-subscribed-notifications', False),
                ]),
            ],
            'ietf-subscribed-notifications',
            'subscription',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'SubscriptionConfig' : {
        'meta_info' : _MetaInfoClass('SubscriptionConfig',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.ietf.ietf_subscribed_notifications', 'SubscriptionConfig.Subscription', 
                [], [], 
                '''                Content of a subscription.
                ''',
                'subscription',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'subscription-config',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'Subscriptions.Subscription.Receivers.Receiver' : {
        'meta_info' : _MetaInfoClass('Subscriptions.Subscription.Receivers.Receiver',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specifies the address for the traffic to reach a remote
                host. One of the following must be specified: an ipv4
                address, an ipv6 address, or a host name.
                ''',
                'address',
                'ietf-subscribed-notifications', True, [
                    _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Specifies the address for the traffic to reach a remote
                        host. One of the following must be specified: an ipv4
                        address, an ipv6 address, or a host name.
                        ''',
                        'address',
                        'ietf-subscribed-notifications', True, [
                            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Specifies the address for the traffic to reach a remote
                                host. One of the following must be specified: an ipv4
                                address, an ipv6 address, or a host name.
                                ''',
                                'address',
                                'ietf-subscribed-notifications', True),
                            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Specifies the address for the traffic to reach a remote
                                host. One of the following must be specified: an ipv4
                                address, an ipv6 address, or a host name.
                                ''',
                                'address',
                                'ietf-subscribed-notifications', True),
                        ]),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                        '''                        Specifies the address for the traffic to reach a remote
                        host. One of the following must be specified: an ipv4
                        address, an ipv6 address, or a host name.
                        ''',
                        'address',
                        'ietf-subscribed-notifications', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This leaf specifies the port number to use for messages
                destined for a receiver.
                ''',
                'port',
                'ietf-subscribed-notifications', True),
            _MetaInfoClassMember('protocol', REFERENCE_IDENTITY_CLASS, 'TransportIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'TransportIdentity', 
                [], [], 
                '''                This leaf specifies the transport protocol used
                to deliver messages destined for the receiver.  Each
                protocol may use the address and port information
                differently as applicable.
                ''',
                'protocol',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('pushed-notifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Operational data which provides the number of update
                notifications pushed to a receiver.
                ''',
                'pushed_notifications',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('excluded-notifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Operational data which provides the number of non-
                datastore update notifications explicitly removed via
                filtering so that they are not sent to a receiver.
                ''',
                'excluded_notifications',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'receiver',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'Subscriptions.Subscription.Receivers' : {
        'meta_info' : _MetaInfoClass('Subscriptions.Subscription.Receivers',
            False, 
            [
            _MetaInfoClassMember('receiver', REFERENCE_LIST, 'Receiver' , 'ydk.models.ietf.ietf_subscribed_notifications', 'Subscriptions.Subscription.Receivers.Receiver', 
                [], [], 
                '''                A single host or multipoint address intended as a target
                for the notifications for a subscription.
                ''',
                'receiver',
                'ietf-subscribed-notifications', False, min_elements=1),
            ],
            'ietf-subscribed-notifications',
            'receivers',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'Subscriptions.Subscription' : {
        'meta_info' : _MetaInfoClass('Subscriptions.Subscription',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier of this subscription.
                ''',
                'identifier',
                'ietf-subscribed-notifications', True),
            _MetaInfoClassMember('configured-subscription', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The presence of this leaf indicates that the subscription
                originated from configuration, not through a control channel
                or RPC.
                ''',
                'configured_subscription',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('stream', REFERENCE_IDENTITY_CLASS, 'StreamIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'StreamIdentity', 
                [], [], 
                '''                Indicates which stream of events is of interest.
                If not present, events in the default NETCONF stream
                will be sent.
                ''',
                'stream',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('encoding', REFERENCE_IDENTITY_CLASS, 'EncodingsIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'EncodingsIdentity', 
                [], [], 
                '''                The type of encoding for the subscribed data.
                Default is XML
                ''',
                'encoding',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('replay-start-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Used to trigger the replay feature and indicate that the
                replay should start at the time specified.  If replay-start-time
                is not present, this is not a replay subscription and event
                pushes should start immediately.  It is never valid to
                specify start times that are later than or equal to the
                current time.
                ''',
                'replay_start_time',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('stop-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Identifies a time after which notification events should not
                be sent.  If stop-time is not present, the notifications will
                continue until the subscription is terminated.  If
                replay-start-time exists, stop-time must for a subsequent time.
                If replay-start-time doesn't exist, stop-time must for a future
                time.
                ''',
                'stop_time',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                References an existing filter which is to be applied to
                the potential events of the subscription.
                ''',
                'filter_ref',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('filter', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Filter which excludes whole event-notifications. If a filter
                element is specified to look for data of a particular
                value, and the data item is not present within a particular
                event notification for its value to be checked against, the
                notification will be filtered  out. For example, if one
                were to check for 'severity=critical' in a configuration
                event notification where this field was not supported, then
                the notification would be filtered out. For subtree
                filtering, a non-empty node set means that the filter
                matches.  For XPath filtering, the mechanisms defined in
                [XPATH] should be used to convert the returned  value to
                boolean.
                ''',
                'filter',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References the interface for notifications.
                ''',
                'source_interface',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('source-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Network instance name for the VRF.  This could also have
                been a leafref to draft-ietf-rtgwg-ni-model, but that model
                in not complete, and may not be implemented on a box.
                ''',
                'source_vrf',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The source address for the notifications.
                ''',
                'source_address',
                'ietf-subscribed-notifications', False, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The source address for the notifications.
                        ''',
                        'source_address',
                        'ietf-subscribed-notifications', False),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The source address for the notifications.
                        ''',
                        'source_address',
                        'ietf-subscribed-notifications', False),
                ]),
            _MetaInfoClassMember('receivers', REFERENCE_CLASS, 'Receivers' , 'ydk.models.ietf.ietf_subscribed_notifications', 'Subscriptions.Subscription.Receivers', 
                [], [], 
                '''                Set of receivers in a subscription.
                ''',
                'receivers',
                'ietf-subscribed-notifications', False),
            _MetaInfoClassMember('subscription-status', REFERENCE_IDENTITY_CLASS, 'SubscriptionStreamStatusIdentity' , 'ydk.models.ietf.ietf_subscribed_notifications', 'SubscriptionStreamStatusIdentity', 
                [], [], 
                '''                The status of the subscription.
                ''',
                'subscription_status',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'subscription',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'Subscriptions' : {
        'meta_info' : _MetaInfoClass('Subscriptions',
            False, 
            [
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.ietf.ietf_subscribed_notifications', 'Subscriptions.Subscription', 
                [], [], 
                '''                Content of a subscription.
                Subscriptions can be created using a control channel or RPC, or
                be established through configuration.
                ''',
                'subscription',
                'ietf-subscribed-notifications', False),
            ],
            'ietf-subscribed-notifications',
            'subscriptions',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'SuspendedIdentity' : {
        'meta_info' : _MetaInfoClass('SuspendedIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'suspended',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'EncodeJsonIdentity' : {
        'meta_info' : _MetaInfoClass('EncodeJsonIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'encode-json',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'InErrorIdentity' : {
        'meta_info' : _MetaInfoClass('InErrorIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'in-error',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'NetconfIdentity' : {
        'meta_info' : _MetaInfoClass('NetconfIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'netconf',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'ErrorIdentity' : {
        'meta_info' : _MetaInfoClass('ErrorIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'error',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'ActiveIdentity' : {
        'meta_info' : _MetaInfoClass('ActiveIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'active',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'HistoryUnavailableIdentity' : {
        'meta_info' : _MetaInfoClass('HistoryUnavailableIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'history-unavailable',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'NamespaceUnavailableIdentity' : {
        'meta_info' : _MetaInfoClass('NamespaceUnavailableIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'namespace-unavailable',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'NetconfIdentity' : {
        'meta_info' : _MetaInfoClass('NetconfIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'NETCONF',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'OkIdentity' : {
        'meta_info' : _MetaInfoClass('OkIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'ok',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'EncodeXmlIdentity' : {
        'meta_info' : _MetaInfoClass('EncodeXmlIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'encode-xml',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'SuspensionTimeoutIdentity' : {
        'meta_info' : _MetaInfoClass('SuspensionTimeoutIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'suspension-timeout',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'InactiveIdentity' : {
        'meta_info' : _MetaInfoClass('InactiveIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'inactive',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'NoSuchSubscriptionIdentity' : {
        'meta_info' : _MetaInfoClass('NoSuchSubscriptionIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'no-such-subscription',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'EncodingUnavailableIdentity' : {
        'meta_info' : _MetaInfoClass('EncodingUnavailableIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'encoding-unavailable',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'ReplayUnsupportedIdentity' : {
        'meta_info' : _MetaInfoClass('ReplayUnsupportedIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'replay-unsupported',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'StreamUnavailableIdentity' : {
        'meta_info' : _MetaInfoClass('StreamUnavailableIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'stream-unavailable',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'InternalErrorIdentity' : {
        'meta_info' : _MetaInfoClass('InternalErrorIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'internal-error',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'FilterUnavailableIdentity' : {
        'meta_info' : _MetaInfoClass('FilterUnavailableIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'filter-unavailable',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
    'FilterUnsupportedIdentity' : {
        'meta_info' : _MetaInfoClass('FilterUnsupportedIdentity',
            False, 
            [
            ],
            'ietf-subscribed-notifications',
            'filter-unsupported',
            _yang_ns._namespaces['ietf-subscribed-notifications'],
        'ydk.models.ietf.ietf_subscribed_notifications'
        ),
    },
}
_meta_table['EstablishSubscriptionRpc.Input']['meta_info'].parent =_meta_table['EstablishSubscriptionRpc']['meta_info']
_meta_table['EstablishSubscriptionRpc.Output']['meta_info'].parent =_meta_table['EstablishSubscriptionRpc']['meta_info']
_meta_table['ModifySubscriptionRpc.Input']['meta_info'].parent =_meta_table['ModifySubscriptionRpc']['meta_info']
_meta_table['ModifySubscriptionRpc.Output']['meta_info'].parent =_meta_table['ModifySubscriptionRpc']['meta_info']
_meta_table['DeleteSubscriptionRpc.Input']['meta_info'].parent =_meta_table['DeleteSubscriptionRpc']['meta_info']
_meta_table['DeleteSubscriptionRpc.Output']['meta_info'].parent =_meta_table['DeleteSubscriptionRpc']['meta_info']
_meta_table['KillSubscriptionRpc.Input']['meta_info'].parent =_meta_table['KillSubscriptionRpc']['meta_info']
_meta_table['KillSubscriptionRpc.Output']['meta_info'].parent =_meta_table['KillSubscriptionRpc']['meta_info']
_meta_table['Filters.Filter']['meta_info'].parent =_meta_table['Filters']['meta_info']
_meta_table['SubscriptionConfig.Subscription.Receivers.Receiver']['meta_info'].parent =_meta_table['SubscriptionConfig.Subscription.Receivers']['meta_info']
_meta_table['SubscriptionConfig.Subscription.Receivers']['meta_info'].parent =_meta_table['SubscriptionConfig.Subscription']['meta_info']
_meta_table['SubscriptionConfig.Subscription']['meta_info'].parent =_meta_table['SubscriptionConfig']['meta_info']
_meta_table['Subscriptions.Subscription.Receivers.Receiver']['meta_info'].parent =_meta_table['Subscriptions.Subscription.Receivers']['meta_info']
_meta_table['Subscriptions.Subscription.Receivers']['meta_info'].parent =_meta_table['Subscriptions.Subscription']['meta_info']
_meta_table['Subscriptions.Subscription']['meta_info'].parent =_meta_table['Subscriptions']['meta_info']
