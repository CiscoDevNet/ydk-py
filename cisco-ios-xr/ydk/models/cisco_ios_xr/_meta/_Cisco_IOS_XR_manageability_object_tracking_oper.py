


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TrackEnum' : _MetaInfoEnum('TrackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper',
        {
            'interface-type':'interface_type',
            'route-type':'route_type',
            'bool-and-type':'bool_and_type',
            'bool-or-type':'bool_or_type',
            'ipsla-type':'ipsla_type',
            'undefined-type':'undefined_type',
            'threshold-weight':'threshold_weight',
            'threshold-percentage':'threshold_percentage',
            'bfd-type':'bfd_type',
        }, 'Cisco-IOS-XR-manageability-object-tracking-oper', _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper']),
    'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'route-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks',
            False, 
            [
            _MetaInfoClassMember('ipsla-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Op Id
                ''',
                'ipsla_op_id',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest Return Code
                ''',
                'return_code',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest RTT
                ''',
                'rtt',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'ipsla-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks',
            False, 
            [
            _MetaInfoClassMember('debounce-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Debounce Count
                ''',
                'debounce_count',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate
                ''',
                'rate',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bfd-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo',
            False, 
            [
            _MetaInfoClassMember('bfd-tracks', REFERENCE_CLASS, 'BfdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks', 
                [], [], 
                '''                track type bfdrtr info
                ''',
                'bfd_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('discriminant', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                discriminant
                ''',
                'discriminant',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-tracks', REFERENCE_CLASS, 'InterfaceTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks', 
                [], [], 
                '''                track type interface info
                ''',
                'interface_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('ipsla-tracks', REFERENCE_CLASS, 'IpslaTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks', 
                [], [], 
                '''                track type rtr info
                ''',
                'ipsla_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('route-tracks', REFERENCE_CLASS, 'RouteTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks', 
                [], [], 
                '''                track type route info
                ''',
                'route_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Object Name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('with-not', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track object with Not
                ''',
                'with_not',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bool-track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks',
            False, 
            [
            _MetaInfoClassMember('bool-track-info', REFERENCE_LIST, 'BoolTrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo', 
                [], [], 
                '''                bool track info
                ''',
                'bool_track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bool-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Object name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state. True means track is up; False
                means track is down.
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Weight is the number assigned to a track object
                . In case of a type threshold weight( i.e.
                weighted sum list), weight is asigned by User
                at the time of configuration. In case of a type
                threshold percentage (i.e. percentage based
                list), weight is internally computed by
                (1/N)x100, where N is the number of objects in
                the list.
                ''',
                'weight',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'threshold-track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks',
            False, 
            [
            _MetaInfoClassMember('threshold-track-info', REFERENCE_LIST, 'ThresholdTrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo', 
                [], [], 
                '''                threshold track info
                ''',
                'threshold_track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'threshold-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracking-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces',
            False, 
            [
            _MetaInfoClassMember('interface-tracking-info', REFERENCE_LIST, 'InterfaceTrackingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo', 
                [], [], 
                '''                interface tracking info
                ''',
                'interface_tracking_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'tracking-interaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo.Delayed' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo.Delayed',
            False, 
            [
            _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining in seconds for the counter to
                trigger state change
                ''',
                'time_remaining',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                State the track will transition to. Track state.
                True means track is up; False means track is
                down.
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'delayed',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface.TrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface.TrackInfo',
            False, 
            [
            _MetaInfoClassMember('bool-tracks', REFERENCE_CLASS, 'BoolTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks', 
                [], [], 
                '''                boolean objects
                ''',
                'bool_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('delayed', REFERENCE_CLASS, 'Delayed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.Delayed', 
                [], [], 
                '''                Is the state change delay counter in progress
                ''',
                'delayed',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('seconds-last-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Seconds Last Change
                ''',
                'seconds_last_change',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('state-change-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State Change Counter
                ''',
                'state_change_counter',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                User specified threshold lower limit
                ''',
                'threshold_down',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-tracks', REFERENCE_CLASS, 'ThresholdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks', 
                [], [], 
                '''                Threshold objects
                ''',
                'threshold_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                User specified threshold upper limit
                ''',
                'threshold_up',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-info', REFERENCE_CLASS, 'TrackTypeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo', 
                [], [], 
                '''                Track type information
                ''',
                'track_type_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracke-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track Name
                ''',
                'tracke_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracking-interaces', REFERENCE_CLASS, 'TrackingInteraces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces', 
                [], [], 
                '''                Tracking Interfaces
                ''',
                'tracking_interaces',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                Track type
                ''',
                'type',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterface' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterface',
            False, 
            [
            _MetaInfoClassMember('track-info', REFERENCE_LIST, 'TrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface.TrackInfo', 
                [], [], 
                '''                track info
                ''',
                'track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'route-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks',
            False, 
            [
            _MetaInfoClassMember('ipsla-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Op Id
                ''',
                'ipsla_op_id',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest Return Code
                ''',
                'return_code',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest RTT
                ''',
                'rtt',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'ipsla-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks',
            False, 
            [
            _MetaInfoClassMember('debounce-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Debounce Count
                ''',
                'debounce_count',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate
                ''',
                'rate',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bfd-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo',
            False, 
            [
            _MetaInfoClassMember('bfd-tracks', REFERENCE_CLASS, 'BfdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks', 
                [], [], 
                '''                track type bfdrtr info
                ''',
                'bfd_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('discriminant', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                discriminant
                ''',
                'discriminant',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-tracks', REFERENCE_CLASS, 'InterfaceTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks', 
                [], [], 
                '''                track type interface info
                ''',
                'interface_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('ipsla-tracks', REFERENCE_CLASS, 'IpslaTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks', 
                [], [], 
                '''                track type rtr info
                ''',
                'ipsla_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('route-tracks', REFERENCE_CLASS, 'RouteTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks', 
                [], [], 
                '''                track type route info
                ''',
                'route_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief',
            False, 
            [
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-info', REFERENCE_CLASS, 'TrackTypeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo', 
                [], [], 
                '''                Track type information
                ''',
                'track_type_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracke-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track Name
                ''',
                'tracke_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                Track type
                ''',
                'type',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-info-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackBriefs.TrackBrief' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackBriefs.TrackBrief',
            False, 
            [
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Track name
                ''',
                'track_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', True),
            _MetaInfoClassMember('track-info-brief', REFERENCE_LIST, 'TrackInfoBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief', 
                [], [], 
                '''                track info brief
                ''',
                'track_info_brief',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackBriefs' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackBriefs',
            False, 
            [
            _MetaInfoClassMember('track-brief', REFERENCE_LIST, 'TrackBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackBriefs.TrackBrief', 
                [], [], 
                '''                Track name - maximum 32 characters
                ''',
                'track_brief',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'route-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks',
            False, 
            [
            _MetaInfoClassMember('ipsla-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Op Id
                ''',
                'ipsla_op_id',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest Return Code
                ''',
                'return_code',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest RTT
                ''',
                'rtt',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'ipsla-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks',
            False, 
            [
            _MetaInfoClassMember('debounce-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Debounce Count
                ''',
                'debounce_count',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate
                ''',
                'rate',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bfd-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo',
            False, 
            [
            _MetaInfoClassMember('bfd-tracks', REFERENCE_CLASS, 'BfdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks', 
                [], [], 
                '''                track type bfdrtr info
                ''',
                'bfd_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('discriminant', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                discriminant
                ''',
                'discriminant',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-tracks', REFERENCE_CLASS, 'InterfaceTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks', 
                [], [], 
                '''                track type interface info
                ''',
                'interface_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('ipsla-tracks', REFERENCE_CLASS, 'IpslaTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks', 
                [], [], 
                '''                track type rtr info
                ''',
                'ipsla_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('route-tracks', REFERENCE_CLASS, 'RouteTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks', 
                [], [], 
                '''                track type route info
                ''',
                'route_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Object Name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('with-not', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track object with Not
                ''',
                'with_not',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bool-track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks',
            False, 
            [
            _MetaInfoClassMember('bool-track-info', REFERENCE_LIST, 'BoolTrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo', 
                [], [], 
                '''                bool track info
                ''',
                'bool_track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bool-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Object name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state. True means track is up; False
                means track is down.
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Weight is the number assigned to a track object
                . In case of a type threshold weight( i.e.
                weighted sum list), weight is asigned by User
                at the time of configuration. In case of a type
                threshold percentage (i.e. percentage based
                list), weight is internally computed by
                (1/N)x100, where N is the number of objects in
                the list.
                ''',
                'weight',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'threshold-track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks',
            False, 
            [
            _MetaInfoClassMember('threshold-track-info', REFERENCE_LIST, 'ThresholdTrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo', 
                [], [], 
                '''                threshold track info
                ''',
                'threshold_track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'threshold-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracking-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces',
            False, 
            [
            _MetaInfoClassMember('interface-tracking-info', REFERENCE_LIST, 'InterfaceTrackingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo', 
                [], [], 
                '''                interface tracking info
                ''',
                'interface_tracking_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'tracking-interaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed',
            False, 
            [
            _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining in seconds for the counter to
                trigger state change
                ''',
                'time_remaining',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                State the track will transition to. Track state.
                True means track is up; False means track is
                down.
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'delayed',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability.TrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability.TrackInfo',
            False, 
            [
            _MetaInfoClassMember('bool-tracks', REFERENCE_CLASS, 'BoolTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks', 
                [], [], 
                '''                boolean objects
                ''',
                'bool_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('delayed', REFERENCE_CLASS, 'Delayed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed', 
                [], [], 
                '''                Is the state change delay counter in progress
                ''',
                'delayed',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('seconds-last-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Seconds Last Change
                ''',
                'seconds_last_change',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('state-change-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State Change Counter
                ''',
                'state_change_counter',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                User specified threshold lower limit
                ''',
                'threshold_down',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-tracks', REFERENCE_CLASS, 'ThresholdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks', 
                [], [], 
                '''                Threshold objects
                ''',
                'threshold_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                User specified threshold upper limit
                ''',
                'threshold_up',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-info', REFERENCE_CLASS, 'TrackTypeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo', 
                [], [], 
                '''                Track type information
                ''',
                'track_type_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracke-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track Name
                ''',
                'tracke_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracking-interaces', REFERENCE_CLASS, 'TrackingInteraces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces', 
                [], [], 
                '''                Tracking Interfaces
                ''',
                'tracking_interaces',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                Track type
                ''',
                'type',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachability' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachability',
            False, 
            [
            _MetaInfoClassMember('track-info', REFERENCE_LIST, 'TrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability.TrackInfo', 
                [], [], 
                '''                track info
                ''',
                'track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-rtr-reachability',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'route-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks',
            False, 
            [
            _MetaInfoClassMember('ipsla-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Op Id
                ''',
                'ipsla_op_id',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest Return Code
                ''',
                'return_code',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest RTT
                ''',
                'rtt',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'ipsla-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks',
            False, 
            [
            _MetaInfoClassMember('debounce-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Debounce Count
                ''',
                'debounce_count',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate
                ''',
                'rate',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bfd-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo',
            False, 
            [
            _MetaInfoClassMember('bfd-tracks', REFERENCE_CLASS, 'BfdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks', 
                [], [], 
                '''                track type bfdrtr info
                ''',
                'bfd_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('discriminant', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                discriminant
                ''',
                'discriminant',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-tracks', REFERENCE_CLASS, 'InterfaceTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks', 
                [], [], 
                '''                track type interface info
                ''',
                'interface_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('ipsla-tracks', REFERENCE_CLASS, 'IpslaTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks', 
                [], [], 
                '''                track type rtr info
                ''',
                'ipsla_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('route-tracks', REFERENCE_CLASS, 'RouteTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks', 
                [], [], 
                '''                track type route info
                ''',
                'route_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief',
            False, 
            [
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-info', REFERENCE_CLASS, 'TrackTypeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo', 
                [], [], 
                '''                Track type information
                ''',
                'track_type_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracke-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track Name
                ''',
                'tracke_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                Track type
                ''',
                'type',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-info-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeRtrReachabilityBrief' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeRtrReachabilityBrief',
            False, 
            [
            _MetaInfoClassMember('track-info-brief', REFERENCE_LIST, 'TrackInfoBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief', 
                [], [], 
                '''                track info brief
                ''',
                'track_info_brief',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-rtr-reachability-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'route-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks',
            False, 
            [
            _MetaInfoClassMember('ipsla-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Op Id
                ''',
                'ipsla_op_id',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest Return Code
                ''',
                'return_code',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest RTT
                ''',
                'rtt',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'ipsla-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks',
            False, 
            [
            _MetaInfoClassMember('debounce-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Debounce Count
                ''',
                'debounce_count',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate
                ''',
                'rate',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bfd-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo',
            False, 
            [
            _MetaInfoClassMember('bfd-tracks', REFERENCE_CLASS, 'BfdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks', 
                [], [], 
                '''                track type bfdrtr info
                ''',
                'bfd_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('discriminant', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                discriminant
                ''',
                'discriminant',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-tracks', REFERENCE_CLASS, 'InterfaceTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks', 
                [], [], 
                '''                track type interface info
                ''',
                'interface_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('ipsla-tracks', REFERENCE_CLASS, 'IpslaTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks', 
                [], [], 
                '''                track type rtr info
                ''',
                'ipsla_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('route-tracks', REFERENCE_CLASS, 'RouteTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks', 
                [], [], 
                '''                track type route info
                ''',
                'route_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Object Name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('with-not', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track object with Not
                ''',
                'with_not',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bool-track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.BoolTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.BoolTracks',
            False, 
            [
            _MetaInfoClassMember('bool-track-info', REFERENCE_LIST, 'BoolTrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo', 
                [], [], 
                '''                bool track info
                ''',
                'bool_track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bool-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Object name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state. True means track is up; False
                means track is down.
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Weight is the number assigned to a track object
                . In case of a type threshold weight( i.e.
                weighted sum list), weight is asigned by User
                at the time of configuration. In case of a type
                threshold percentage (i.e. percentage based
                list), weight is internally computed by
                (1/N)x100, where N is the number of objects in
                the list.
                ''',
                'weight',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'threshold-track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks',
            False, 
            [
            _MetaInfoClassMember('threshold-track-info', REFERENCE_LIST, 'ThresholdTrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo', 
                [], [], 
                '''                threshold track info
                ''',
                'threshold_track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'threshold-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracking-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces',
            False, 
            [
            _MetaInfoClassMember('interface-tracking-info', REFERENCE_LIST, 'InterfaceTrackingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo', 
                [], [], 
                '''                interface tracking info
                ''',
                'interface_tracking_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'tracking-interaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo.Delayed' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo.Delayed',
            False, 
            [
            _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining in seconds for the counter to
                trigger state change
                ''',
                'time_remaining',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                State the track will transition to. Track state.
                True means track is up; False means track is
                down.
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'delayed',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track.TrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track.TrackInfo',
            False, 
            [
            _MetaInfoClassMember('bool-tracks', REFERENCE_CLASS, 'BoolTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.BoolTracks', 
                [], [], 
                '''                boolean objects
                ''',
                'bool_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('delayed', REFERENCE_CLASS, 'Delayed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.Delayed', 
                [], [], 
                '''                Is the state change delay counter in progress
                ''',
                'delayed',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('seconds-last-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Seconds Last Change
                ''',
                'seconds_last_change',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('state-change-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State Change Counter
                ''',
                'state_change_counter',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                User specified threshold lower limit
                ''',
                'threshold_down',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-tracks', REFERENCE_CLASS, 'ThresholdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks', 
                [], [], 
                '''                Threshold objects
                ''',
                'threshold_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                User specified threshold upper limit
                ''',
                'threshold_up',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-info', REFERENCE_CLASS, 'TrackTypeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo', 
                [], [], 
                '''                Track type information
                ''',
                'track_type_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracke-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track Name
                ''',
                'tracke_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracking-interaces', REFERENCE_CLASS, 'TrackingInteraces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces', 
                [], [], 
                '''                Tracking Interfaces
                ''',
                'tracking_interaces',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                Track type
                ''',
                'type',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks.Track' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks.Track',
            False, 
            [
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Track name
                ''',
                'track_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', True),
            _MetaInfoClassMember('track-info', REFERENCE_LIST, 'TrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track.TrackInfo', 
                [], [], 
                '''                track info
                ''',
                'track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.Tracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.Tracks',
            False, 
            [
            _MetaInfoClassMember('track', REFERENCE_LIST, 'Track' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks.Track', 
                [], [], 
                '''                Track name - maximum 32 characters
                ''',
                'track',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'route-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks',
            False, 
            [
            _MetaInfoClassMember('ipsla-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Op Id
                ''',
                'ipsla_op_id',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest Return Code
                ''',
                'return_code',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest RTT
                ''',
                'rtt',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'ipsla-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks',
            False, 
            [
            _MetaInfoClassMember('debounce-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Debounce Count
                ''',
                'debounce_count',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate
                ''',
                'rate',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bfd-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo',
            False, 
            [
            _MetaInfoClassMember('bfd-tracks', REFERENCE_CLASS, 'BfdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks', 
                [], [], 
                '''                track type bfdrtr info
                ''',
                'bfd_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('discriminant', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                discriminant
                ''',
                'discriminant',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-tracks', REFERENCE_CLASS, 'InterfaceTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks', 
                [], [], 
                '''                track type interface info
                ''',
                'interface_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('ipsla-tracks', REFERENCE_CLASS, 'IpslaTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks', 
                [], [], 
                '''                track type rtr info
                ''',
                'ipsla_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('route-tracks', REFERENCE_CLASS, 'RouteTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks', 
                [], [], 
                '''                track type route info
                ''',
                'route_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief',
            False, 
            [
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-info', REFERENCE_CLASS, 'TrackTypeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo', 
                [], [], 
                '''                Track type information
                ''',
                'track_type_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracke-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track Name
                ''',
                'tracke_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                Track type
                ''',
                'type',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-info-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4RouteBrief' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4RouteBrief',
            False, 
            [
            _MetaInfoClassMember('track-info-brief', REFERENCE_LIST, 'TrackInfoBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief', 
                [], [], 
                '''                track info brief
                ''',
                'track_info_brief',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-ipv4-route-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'route-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks',
            False, 
            [
            _MetaInfoClassMember('ipsla-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Op Id
                ''',
                'ipsla_op_id',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest Return Code
                ''',
                'return_code',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest RTT
                ''',
                'rtt',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'ipsla-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks',
            False, 
            [
            _MetaInfoClassMember('debounce-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Debounce Count
                ''',
                'debounce_count',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate
                ''',
                'rate',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bfd-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo',
            False, 
            [
            _MetaInfoClassMember('bfd-tracks', REFERENCE_CLASS, 'BfdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks', 
                [], [], 
                '''                track type bfdrtr info
                ''',
                'bfd_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('discriminant', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                discriminant
                ''',
                'discriminant',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-tracks', REFERENCE_CLASS, 'InterfaceTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks', 
                [], [], 
                '''                track type interface info
                ''',
                'interface_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('ipsla-tracks', REFERENCE_CLASS, 'IpslaTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks', 
                [], [], 
                '''                track type rtr info
                ''',
                'ipsla_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('route-tracks', REFERENCE_CLASS, 'RouteTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks', 
                [], [], 
                '''                track type route info
                ''',
                'route_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Object Name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('with-not', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track object with Not
                ''',
                'with_not',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bool-track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks',
            False, 
            [
            _MetaInfoClassMember('bool-track-info', REFERENCE_LIST, 'BoolTrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo', 
                [], [], 
                '''                bool track info
                ''',
                'bool_track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bool-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Object name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state. True means track is up; False
                means track is down.
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Weight is the number assigned to a track object
                . In case of a type threshold weight( i.e.
                weighted sum list), weight is asigned by User
                at the time of configuration. In case of a type
                threshold percentage (i.e. percentage based
                list), weight is internally computed by
                (1/N)x100, where N is the number of objects in
                the list.
                ''',
                'weight',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'threshold-track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks',
            False, 
            [
            _MetaInfoClassMember('threshold-track-info', REFERENCE_LIST, 'ThresholdTrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo', 
                [], [], 
                '''                threshold track info
                ''',
                'threshold_track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'threshold-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracking-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces',
            False, 
            [
            _MetaInfoClassMember('interface-tracking-info', REFERENCE_LIST, 'InterfaceTrackingInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo', 
                [], [], 
                '''                interface tracking info
                ''',
                'interface_tracking_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'tracking-interaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed',
            False, 
            [
            _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time remaining in seconds for the counter to
                trigger state change
                ''',
                'time_remaining',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                State the track will transition to. Track state.
                True means track is up; False means track is
                down.
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'delayed',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route.TrackInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route.TrackInfo',
            False, 
            [
            _MetaInfoClassMember('bool-tracks', REFERENCE_CLASS, 'BoolTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks', 
                [], [], 
                '''                boolean objects
                ''',
                'bool_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('delayed', REFERENCE_CLASS, 'Delayed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed', 
                [], [], 
                '''                Is the state change delay counter in progress
                ''',
                'delayed',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('seconds-last-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Seconds Last Change
                ''',
                'seconds_last_change',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('state-change-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State Change Counter
                ''',
                'state_change_counter',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                User specified threshold lower limit
                ''',
                'threshold_down',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-tracks', REFERENCE_CLASS, 'ThresholdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks', 
                [], [], 
                '''                Threshold objects
                ''',
                'threshold_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('threshold-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                User specified threshold upper limit
                ''',
                'threshold_up',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-info', REFERENCE_CLASS, 'TrackTypeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo', 
                [], [], 
                '''                Track type information
                ''',
                'track_type_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracke-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track Name
                ''',
                'tracke_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracking-interaces', REFERENCE_CLASS, 'TrackingInteraces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces', 
                [], [], 
                '''                Tracking Interfaces
                ''',
                'tracking_interaces',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                Track type
                ''',
                'type',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeIpv4Route' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeIpv4Route',
            False, 
            [
            _MetaInfoClassMember('track-info', REFERENCE_LIST, 'TrackInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route.TrackInfo', 
                [], [], 
                '''                track info
                ''',
                'track_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-ipv4-route',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'interface-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'route-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks',
            False, 
            [
            _MetaInfoClassMember('ipsla-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Op Id
                ''',
                'ipsla_op_id',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('return-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest Return Code
                ''',
                'return_code',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest RTT
                ''',
                'rtt',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'ipsla-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks',
            False, 
            [
            _MetaInfoClassMember('debounce-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Debounce Count
                ''',
                'debounce_count',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination Address
                ''',
                'destination_address',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 120)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate
                ''',
                'rate',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'bfd-tracks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo',
            False, 
            [
            _MetaInfoClassMember('bfd-tracks', REFERENCE_CLASS, 'BfdTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks', 
                [], [], 
                '''                track type bfdrtr info
                ''',
                'bfd_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('discriminant', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                discriminant
                ''',
                'discriminant',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('interface-tracks', REFERENCE_CLASS, 'InterfaceTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks', 
                [], [], 
                '''                track type interface info
                ''',
                'interface_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('ipsla-tracks', REFERENCE_CLASS, 'IpslaTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks', 
                [], [], 
                '''                track type rtr info
                ''',
                'ipsla_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('route-tracks', REFERENCE_CLASS, 'RouteTracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks', 
                [], [], 
                '''                track type route info
                ''',
                'route_tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-info',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief',
            False, 
            [
            _MetaInfoClassMember('track-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Track state
                ''',
                'track_state',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-info', REFERENCE_CLASS, 'TrackTypeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo', 
                [], [], 
                '''                Track type information
                ''',
                'track_type_info',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracke-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track Name
                ''',
                'tracke_name',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TrackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'TrackEnum', 
                [], [], 
                '''                Track type
                ''',
                'type',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-info-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking.TrackTypeInterfaceBrief' : {
        'meta_info' : _MetaInfoClass('ObjectTracking.TrackTypeInterfaceBrief',
            False, 
            [
            _MetaInfoClassMember('track-info-brief', REFERENCE_LIST, 'TrackInfoBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief', 
                [], [], 
                '''                track info brief
                ''',
                'track_info_brief',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'track-type-interface-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
    'ObjectTracking' : {
        'meta_info' : _MetaInfoClass('ObjectTracking',
            False, 
            [
            _MetaInfoClassMember('track-briefs', REFERENCE_CLASS, 'TrackBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackBriefs', 
                [], [], 
                '''                Object Tracking Track table brief
                ''',
                'track_briefs',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-interface', REFERENCE_CLASS, 'TrackTypeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterface', 
                [], [], 
                '''                Object Tracking Type interface info
                ''',
                'track_type_interface',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-interface-brief', REFERENCE_CLASS, 'TrackTypeInterfaceBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeInterfaceBrief', 
                [], [], 
                '''                Object Tracking Type Interface brief info
                ''',
                'track_type_interface_brief',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-ipv4-route', REFERENCE_CLASS, 'TrackTypeIpv4Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4Route', 
                [], [], 
                '''                Object Tracking Type IPV4 route info
                ''',
                'track_type_ipv4_route',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-ipv4-route-brief', REFERENCE_CLASS, 'TrackTypeIpv4RouteBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeIpv4RouteBrief', 
                [], [], 
                '''                Object Tracking Type Ipv4 Route brief info
                ''',
                'track_type_ipv4_route_brief',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-rtr-reachability', REFERENCE_CLASS, 'TrackTypeRtrReachability' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachability', 
                [], [], 
                '''                Object Tracking Type RTR Reachability info
                ''',
                'track_type_rtr_reachability',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('track-type-rtr-reachability-brief', REFERENCE_CLASS, 'TrackTypeRtrReachabilityBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.TrackTypeRtrReachabilityBrief', 
                [], [], 
                '''                Object Tracking Type RTR Reachability brief info
                ''',
                'track_type_rtr_reachability_brief',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            _MetaInfoClassMember('tracks', REFERENCE_CLASS, 'Tracks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'ObjectTracking.Tracks', 
                [], [], 
                '''                Object Tracking Track table
                ''',
                'tracks',
                'Cisco-IOS-XR-manageability-object-tracking-oper', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-oper',
            'object-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper'
        ),
    },
}
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.Delayed']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface.TrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterface']['meta_info']
_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief']['meta_info']
_meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief']['meta_info'].parent =_meta_table['ObjectTracking.TrackBriefs.TrackBrief']['meta_info']
_meta_table['ObjectTracking.TrackBriefs.TrackBrief']['meta_info'].parent =_meta_table['ObjectTracking.TrackBriefs']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachability']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo.BoolTracks']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.BoolTracks']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo.Delayed']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track.TrackInfo']['meta_info']
_meta_table['ObjectTracking.Tracks.Track.TrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.Tracks.Track']['meta_info']
_meta_table['ObjectTracking.Tracks.Track']['meta_info'].parent =_meta_table['ObjectTracking.Tracks']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeIpv4Route']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief']['meta_info'].parent =_meta_table['ObjectTracking.TrackTypeInterfaceBrief']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterface']['meta_info'].parent =_meta_table['ObjectTracking']['meta_info']
_meta_table['ObjectTracking.TrackBriefs']['meta_info'].parent =_meta_table['ObjectTracking']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachability']['meta_info'].parent =_meta_table['ObjectTracking']['meta_info']
_meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief']['meta_info'].parent =_meta_table['ObjectTracking']['meta_info']
_meta_table['ObjectTracking.Tracks']['meta_info'].parent =_meta_table['ObjectTracking']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4RouteBrief']['meta_info'].parent =_meta_table['ObjectTracking']['meta_info']
_meta_table['ObjectTracking.TrackTypeIpv4Route']['meta_info'].parent =_meta_table['ObjectTracking']['meta_info']
_meta_table['ObjectTracking.TrackTypeInterfaceBrief']['meta_info'].parent =_meta_table['ObjectTracking']['meta_info']
