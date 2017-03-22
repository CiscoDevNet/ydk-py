
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.State.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.Config.advertise_inactive_routes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.Config.enable_aigp' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', 'true'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.Config.external_compare_router_id' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', False),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.Config.ignore_next_hop_igp_metric' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.State.advertise_inactive_routes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.State.enable_aigp' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', 'true'),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.State.external_compare_router_id' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', False),
        ]
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.State.ignore_next_hop_igp_metric' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config.allow_multiple_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State.allow_multiple_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.ApplyPolicy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.Confederation.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.GracefulRestart.Config.helper_only' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.GracefulRestart.State.helper_only' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.RouteSelectionOptions.Config.advertise_inactive_routes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.RouteSelectionOptions.Config.enable_aigp' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', 'true'),
        ]
    },
    'Bgp.Global_.RouteSelectionOptions.Config.external_compare_router_id' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', False),
        ]
    },
    'Bgp.Global_.RouteSelectionOptions.Config.ignore_next_hop_igp_metric' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.RouteSelectionOptions.State.advertise_inactive_routes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.RouteSelectionOptions.State.enable_aigp' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', 'true'),
        ]
    },
    'Bgp.Global_.RouteSelectionOptions.State.external_compare_router_id' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', False),
        ]
    },
    'Bgp.Global_.RouteSelectionOptions.State.ignore_next_hop_igp_metric' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.UseMultiplePaths.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.UseMultiplePaths.Ebgp.Config.allow_multiple_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Global_.UseMultiplePaths.Ebgp.State.allow_multiple_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AddPaths.Config.receive' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AddPaths.Config.send_max' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AddPaths.State.receive' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AddPaths.State.send_max' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State.advertised' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State.received' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes.installed' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.ApplyPolicy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AsPathOptions.Config.allow_own_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AsPathOptions.Config.replace_peer_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AsPathOptions.State.allow_own_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.AsPathOptions.State.replace_peer_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Config.peer_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Config.remove_private_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Config.route_flap_damping' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Config.send_community' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.ErrorHandling' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.GracefulRestart.Config.helper_only' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.GracefulRestart.State.helper_only' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.GracefulRestart.State.local_restarting' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.GracefulRestart.State.mode' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.GracefulRestart.State.peer_restarting' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.LoggingOptions' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.RouteReflector.Config.route_reflector_client' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.RouteReflector.State.route_reflector_client' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.State.peer_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.State.remove_private_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.State.route_flap_damping' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.State.send_community' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Timers.Config.connect_retry' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Timers.State.connect_retry' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Timers.State.uptime' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Transport.Config.mtu_discovery' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.Transport.State.mtu_discovery' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.Neighbors.Neighbor.UseMultiplePaths' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AddPaths.Config.receive' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AddPaths.Config.send_max' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AddPaths.State.receive' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AddPaths.State.send_max' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config.default_export_policy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config.default_import_policy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State.default_export_policy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State.default_import_policy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.max_prefixes' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('must', 'shutdown_threshold_pct'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.restart_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State.shutdown_threshold_pct' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('default', 75),
            ('must', 'max_prefixes'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config.advertise_inactive_routes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config.enable_aigp' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', 'true'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config.external_compare_router_id' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', False),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config.ignore_next_hop_igp_metric' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State.advertise_inactive_routes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State.enable_aigp' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', 'true'),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State.external_compare_router_id' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('default', False),
        ]
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State.ignore_next_hop_igp_metric' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.ApplyPolicy' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AsPathOptions.Config.allow_own_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AsPathOptions.Config.replace_peer_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AsPathOptions.State.allow_own_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.AsPathOptions.State.replace_peer_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.Config.peer_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.Config.remove_private_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.Config.route_flap_damping' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.Config.send_community' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.ErrorHandling.Config.treat_as_withdraw' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.ErrorHandling.State.treat_as_withdraw' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.GracefulRestart.Config.helper_only' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.GracefulRestart.State.helper_only' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.LoggingOptions.Config.log_neighbor_state_changes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.LoggingOptions.State.log_neighbor_state_changes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.RouteReflector.Config.route_reflector_client' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.RouteReflector.State.route_reflector_client' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.State.peer_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.State.remove_private_as' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.State.route_flap_damping' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.State.send_community' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.State.total_paths' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.State.total_prefixes' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.Timers.Config.connect_retry' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.Timers.State.connect_retry' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.Transport.Config.mtu_discovery' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.Transport.State.mtu_discovery' : {
        'deviation_typ' : 'not_supported',
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths' : {
        'deviation_typ' : 'not_supported',
    },
}
