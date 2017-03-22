
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.as4_path' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.as4_path' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.as4_path' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.as4_path' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.as4_path' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.as4_path' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.invalid_reason' : {
        'deviation_typ' : 'not_supported',
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.last_update_received' : {
        'deviation_typ' : 'not_supported',
    },
}
