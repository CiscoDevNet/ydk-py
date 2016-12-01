
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Mpls.Global_.Config.null_label' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Global_.MplsInterfaceAttributes.Interface' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Global_.State.null_label' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config.specification_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State.specification_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Config.description' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Config.preference' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Config.reoptimize_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Config.signaling_protocol' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Config.source' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State.exclude_group' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State.include_all_group' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State.include_any_group' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config.cspf_tiebreaker' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config.hold_priority' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config.retry_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config.setup_priority' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config.use_cspf' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State.cspf_tiebreaker' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State.hold_priority' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State.retry_timer' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State.setup_priority' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State.use_cspf' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.State.preference' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp.fec_address' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.ldp_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.tunnel_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.tunnel_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config.refresh_reduction' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State.refresh_reduction' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config.hello_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State.hello_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config.bypass_optimize_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State.bypass_optimize_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.active_reservation_count' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.highwater_mark' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.SignalingProtocols.SegmentRouting.Srgb' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.down_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.threshold_specification' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.threshold_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.up_down_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.up_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.down_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.threshold_specification' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.threshold_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.up_down_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.up_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg.Config.flooding_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg.State.flooding_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.delta_percentage' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.threshold_specification' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.threshold_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.up_down_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.delta_percentage' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.down_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.threshold_specification' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.threshold_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.up_down_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.up_thresholds' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.State.admin_group' : {
        'deviation_typ' : 'not_supported',
    },
    'Mpls.TeInterfaceAttributes.Interface.State.srlg_membership' : {
        'deviation_typ' : 'not_supported',
    },
}
