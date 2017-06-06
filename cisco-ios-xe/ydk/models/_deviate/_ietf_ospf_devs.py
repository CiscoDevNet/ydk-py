
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance.granularity.coarse' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.bfd' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.demand_circuit' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.enable' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.lls' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.mtu_ignore' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.network_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.node_flag' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.passive' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.prefix_suppression' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity.enable' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.bfd' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.dead_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.enable' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.hello_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.lls' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.mtu_ignore' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.prefix_suppression' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.retransmit_interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.transmit_delay' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity.enable' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.bfd' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.cost' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.enable' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.lls' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.mtu_ignore' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.prefix_suppression' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.area_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.summary' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid.source.explicit' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.enable' : {
        'deviation_typ' : 'not_supported',
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.operation_mode' : {
        'deviation_typ' : 'not_supported',
    },
}
