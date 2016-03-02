


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Device.Acl' : {
        'meta_info' : _MetaInfoClass('Device.Acl',
            False, 
            [
            ],
            'model-structure',
            'acl',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Hardware' : {
        'meta_info' : _MetaInfoClass('Device.Hardware',
            False, 
            [
            ],
            'model-structure',
            'hardware',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Info.DeviceType_Enum' : _MetaInfoEnum('DeviceType_Enum', 'ydk.models.model.model_structure',
        {
            'PHYSICAL':'PHYSICAL',
            'VIRTUAL':'VIRTUAL',
        }, 'model-structure', _yang_ns._namespaces['model-structure']),
    'Device.Info' : {
        'meta_info' : _MetaInfoClass('Device.Info',
            False, 
            [
            _MetaInfoClassMember('device-type', REFERENCE_ENUM_CLASS, 'DeviceType_Enum' , 'ydk.models.model.model_structure', 'Device.Info.DeviceType_Enum', 
                [], [], 
                '''                Type of the device, e.g., physical or virtual.  This node
                may be used to activate other containers in the model
                ''',
                'device_type',
                'model-structure', False),
            ],
            'model-structure',
            'info',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Addressing.Ipv4.Vrrp' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Addressing.Ipv4.Vrrp',
            False, 
            [
            ],
            'model-structure',
            'vrrp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Addressing.Ipv4' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Addressing.Ipv4',
            False, 
            [
            _MetaInfoClassMember('vrrp', REFERENCE_CLASS, 'Vrrp' , 'ydk.models.model.model_structure', 'Device.Interfaces.Addressing.Ipv4.Vrrp', 
                [], [], 
                '''                virtual router redundancy protocol
                ''',
                'vrrp',
                'model-structure', False),
            ],
            'model-structure',
            'ipv4',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Addressing.Ipv6.Vrrp' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Addressing.Ipv6.Vrrp',
            False, 
            [
            ],
            'model-structure',
            'vrrp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Addressing.Ipv6' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Addressing.Ipv6',
            False, 
            [
            _MetaInfoClassMember('vrrp', REFERENCE_CLASS, 'Vrrp' , 'ydk.models.model.model_structure', 'Device.Interfaces.Addressing.Ipv6.Vrrp', 
                [], [], 
                '''                virtual router redundancy protocol
                ''',
                'vrrp',
                'model-structure', False),
            ],
            'model-structure',
            'ipv6',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Addressing' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Addressing',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.model.model_structure', 'Device.Interfaces.Addressing.Ipv4', 
                [], [], 
                '''                IPv4 interfaces
                ''',
                'ipv4',
                'model-structure', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.model.model_structure', 'Device.Interfaces.Addressing.Ipv6', 
                [], [], 
                '''                IPv6 interfaces
                ''',
                'ipv6',
                'model-structure', False),
            ],
            'model-structure',
            'addressing',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Ethernet.Aggregates' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Ethernet.Aggregates',
            False, 
            [
            ],
            'model-structure',
            'aggregates',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Ethernet.Lfm' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Ethernet.Lfm',
            False, 
            [
            ],
            'model-structure',
            'lfm',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Ethernet.Vlans' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Ethernet.Vlans',
            False, 
            [
            ],
            'model-structure',
            'vlans',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Ethernet' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Ethernet',
            False, 
            [
            _MetaInfoClassMember('aggregates', REFERENCE_CLASS, 'Aggregates' , 'ydk.models.model.model_structure', 'Device.Interfaces.Ethernet.Aggregates', 
                [], [], 
                '''                LAGs, LACP, etc. for Ethernet interfaces
                ''',
                'aggregates',
                'model-structure', False),
            _MetaInfoClassMember('lfm', REFERENCE_CLASS, 'Lfm' , 'ydk.models.model.model_structure', 'Device.Interfaces.Ethernet.Lfm', 
                [], [], 
                '''                Link-layer fault management for Ethernet interfaces
                ''',
                'lfm',
                'model-structure', False),
            _MetaInfoClassMember('vlans', REFERENCE_CLASS, 'Vlans' , 'ydk.models.model.model_structure', 'Device.Interfaces.Ethernet.Vlans', 
                [], [], 
                '''                VLANs, 802.1q, q-in-q, etc.
                ''',
                'vlans',
                'model-structure', False),
            ],
            'model-structure',
            'ethernet',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.SonetSdh' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.SonetSdh',
            False, 
            [
            ],
            'model-structure',
            'sonet-sdh',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces.Tunnels' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces.Tunnels',
            False, 
            [
            ],
            'model-structure',
            'tunnels',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Interfaces' : {
        'meta_info' : _MetaInfoClass('Device.Interfaces',
            False, 
            [
            _MetaInfoClassMember('addressing', REFERENCE_CLASS, 'Addressing' , 'ydk.models.model.model_structure', 'Device.Interfaces.Addressing', 
                [], [], 
                '''                addressing and other interface-specific data,
                e.g., data plane protocols
                ''',
                'addressing',
                'model-structure', False),
            _MetaInfoClassMember('ethernet', REFERENCE_CLASS, 'Ethernet' , 'ydk.models.model.model_structure', 'Device.Interfaces.Ethernet', 
                [], [], 
                '''                Ethernet interface config, e.g., 10, 40,
                100GBE
                ''',
                'ethernet',
                'model-structure', False),
            _MetaInfoClassMember('sonet-sdh', REFERENCE_CLASS, 'SonetSdh' , 'ydk.models.model.model_structure', 'Device.Interfaces.SonetSdh', 
                [], [], 
                '''                SONET/SDH interfaces
                ''',
                'sonet_sdh',
                'model-structure', False),
            _MetaInfoClassMember('tunnels', REFERENCE_CLASS, 'Tunnels' , 'ydk.models.model.model_structure', 'Device.Interfaces.Tunnels', 
                [], [], 
                '''                logical tunnel interfaces incl. GRE, VxLAN, L2TP etc.
                ''',
                'tunnels',
                'model-structure', False),
            ],
            'model-structure',
            'interfaces',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Arp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer2Protocols.Arp',
            False, 
            [
            ],
            'model-structure',
            'arp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ipv6Ndp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ipv6Ndp',
            False, 
            [
            ],
            'model-structure',
            'ipv6-ndp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Lldp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer2Protocols.Lldp',
            False, 
            [
            ],
            'model-structure',
            'lldp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ptp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ptp',
            False, 
            [
            ],
            'model-structure',
            'ptp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Rstp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer2Protocols.Rstp',
            False, 
            [
            ],
            'model-structure',
            'rstp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Vsi' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer2Protocols.Vsi',
            False, 
            [
            ],
            'model-structure',
            'vsi',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer2Protocols' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer2Protocols',
            False, 
            [
            _MetaInfoClassMember('arp', REFERENCE_CLASS, 'Arp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Arp', 
                [], [], 
                '''                Address resolution protocol
                ''',
                'arp',
                'model-structure', False),
            _MetaInfoClassMember('ipv6-ndp', REFERENCE_CLASS, 'Ipv6Ndp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ipv6Ndp', 
                [], [], 
                '''                IPv6 neighbor discovery
                ''',
                'ipv6_ndp',
                'model-structure', False),
            _MetaInfoClassMember('lldp', REFERENCE_CLASS, 'Lldp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Lldp', 
                [], [], 
                '''                link layer discovery protocol
                ''',
                'lldp',
                'model-structure', False),
            _MetaInfoClassMember('ptp', REFERENCE_CLASS, 'Ptp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ptp', 
                [], [], 
                '''                precision time protocol for time synchronization services.
                PTP also typically requires per-interface configuration
                ''',
                'ptp',
                'model-structure', False),
            _MetaInfoClassMember('rstp', REFERENCE_CLASS, 'Rstp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Rstp', 
                [], [], 
                '''                rapid spanning tree protocol
                ''',
                'rstp',
                'model-structure', False),
            _MetaInfoClassMember('vsi', REFERENCE_CLASS, 'Vsi' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer2Protocols.Vsi', 
                [], [], 
                '''                virtual switch instance (or virtual forwarding
                instance) for use in PWE3 / VPLS services
                ''',
                'vsi',
                'model-structure', False),
            ],
            'model-structure',
            'layer-2-protocols',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bfd' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bfd',
            False, 
            [
            ],
            'model-structure',
            'bfd',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bgp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bgp',
            False, 
            [
            ],
            'model-structure',
            'bgp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igmp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igmp',
            False, 
            [
            ],
            'model-structure',
            'igmp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IgpCommon' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IgpCommon',
            False, 
            [
            ],
            'model-structure',
            'igp-common',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IsIs' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IsIs',
            False, 
            [
            ],
            'model-structure',
            'is-is',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf2' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf2',
            False, 
            [
            ],
            'model-structure',
            'ospf2',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf3' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf3',
            False, 
            [
            ],
            'model-structure',
            'ospf3',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('ospf2', REFERENCE_CLASS, 'Ospf2' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf2', 
                [], [], 
                '''                OSPF v2
                ''',
                'ospf2',
                'model-structure', False),
            _MetaInfoClassMember('ospf3', REFERENCE_CLASS, 'Ospf3' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf3', 
                [], [], 
                '''                OSPF v3
                ''',
                'ospf3',
                'model-structure', False),
            ],
            'model-structure',
            'ospf',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp',
            False, 
            [
            _MetaInfoClassMember('igp-common', REFERENCE_CLASS, 'IgpCommon' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IgpCommon', 
                [], [], 
                '''                Common parameters for IGP protocols
                ''',
                'igp_common',
                'model-structure', False),
            _MetaInfoClassMember('is-is', REFERENCE_CLASS, 'IsIs' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IsIs', 
                [], [], 
                '''                IS-IS IGP routing protocol
                ''',
                'is_is',
                'model-structure', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf', 
                [], [], 
                '''                OSPF IGP routing protocols
                ''',
                'ospf',
                'model-structure', False),
            ],
            'model-structure',
            'igp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Global' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Global',
            False, 
            [
            ],
            'model-structure',
            'global',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.ConstrainedPath' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.ConstrainedPath',
            False, 
            [
            ],
            'model-structure',
            'constrained-path',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.IgpCongruent' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.IgpCongruent',
            False, 
            [
            ],
            'model-structure',
            'igp-congruent',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.Static' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.Static',
            False, 
            [
            ],
            'model-structure',
            'static',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths',
            False, 
            [
            _MetaInfoClassMember('constrained-path', REFERENCE_CLASS, 'ConstrainedPath' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.ConstrainedPath', 
                [], [], 
                '''                traffic-engineered, or constrained path LSPs
                ''',
                'constrained_path',
                'model-structure', False),
            _MetaInfoClassMember('igp-congruent', REFERENCE_CLASS, 'IgpCongruent' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.IgpCongruent', 
                [], [], 
                '''                LSPs that follow the IGP-computed path
                ''',
                'igp_congruent',
                'model-structure', False),
            _MetaInfoClassMember('static', REFERENCE_CLASS, 'Static' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.Static', 
                [], [], 
                '''                statically configured LSPs
                ''',
                'static',
                'model-structure', False),
            ],
            'model-structure',
            'label-switched-paths',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Ldp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Ldp',
            False, 
            [
            ],
            'model-structure',
            'ldp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Rsvp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Rsvp',
            False, 
            [
            ],
            'model-structure',
            'rsvp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.SegmentRouting',
            False, 
            [
            ],
            'model-structure',
            'segment-routing',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling',
            False, 
            [
            _MetaInfoClassMember('ldp', REFERENCE_CLASS, 'Ldp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Ldp', 
                [], [], 
                '''                label distribution protocol
                ''',
                'ldp',
                'model-structure', False),
            _MetaInfoClassMember('rsvp', REFERENCE_CLASS, 'Rsvp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Rsvp', 
                [], [], 
                '''                RSVP signaling
                ''',
                'rsvp',
                'model-structure', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.SegmentRouting', 
                [], [], 
                '''                SR signaling
                ''',
                'segment_routing',
                'model-structure', False),
            ],
            'model-structure',
            'signaling',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Global', 
                [], [], 
                '''                global MPLS configuration
                ''',
                'global_',
                'model-structure', False),
            _MetaInfoClassMember('label-switched-paths', REFERENCE_CLASS, 'LabelSwitchedPaths' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths', 
                [], [], 
                '''                models for different types of LSPs
                ''',
                'label_switched_paths',
                'model-structure', False),
            _MetaInfoClassMember('signaling', REFERENCE_CLASS, 'Signaling' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling', 
                [], [], 
                '''                MPLS signaling protocols
                ''',
                'signaling',
                'model-structure', False),
            ],
            'model-structure',
            'mpls-te',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Pim' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Pim',
            False, 
            [
            ],
            'model-structure',
            'pim',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.StaticRoutes' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.StaticRoutes',
            False, 
            [
            ],
            'model-structure',
            'static-routes',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global',
            False, 
            [
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bfd', 
                [], [], 
                '''                bidirectional forwarding detection
                ''',
                'bfd',
                'model-structure', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bgp', 
                [], [], 
                '''                BGP 4
                ''',
                'bgp',
                'model-structure', False),
            _MetaInfoClassMember('igmp', REFERENCE_CLASS, 'Igmp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igmp', 
                [], [], 
                '''                Internet group management protocol
                ''',
                'igmp',
                'model-structure', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp', 
                [], [], 
                '''                interior gateway protocols
                ''',
                'igp',
                'model-structure', False),
            _MetaInfoClassMember('mpls-te', REFERENCE_CLASS, 'MplsTe' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe', 
                [], [], 
                '''                MPLS and traffic engineering
                ''',
                'mpls_te',
                'model-structure', False),
            _MetaInfoClassMember('pim', REFERENCE_CLASS, 'Pim' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Pim', 
                [], [], 
                '''                protocol independent multicast
                ''',
                'pim',
                'model-structure', False),
            _MetaInfoClassMember('static-routes', REFERENCE_CLASS, 'StaticRoutes' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.StaticRoutes', 
                [], [], 
                '''                static route that are manually created
                ''',
                'static_routes',
                'model-structure', False),
            ],
            'model-structure',
            'global',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.BgpPolicy' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.BgpPolicy',
            False, 
            [
            ],
            'model-structure',
            'bgp-policy',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.Common' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.Common',
            False, 
            [
            ],
            'model-structure',
            'common',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.IgpPolicy' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.IgpPolicy',
            False, 
            [
            ],
            'model-structure',
            'igp-policy',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.VrfPolicy' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.VrfPolicy',
            False, 
            [
            ],
            'model-structure',
            'vrf-policy',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy',
            False, 
            [
            _MetaInfoClassMember('bgp-policy', REFERENCE_CLASS, 'BgpPolicy' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.BgpPolicy', 
                [], [], 
                '''                BGP-specific routing policy parameters
                ''',
                'bgp_policy',
                'model-structure', False),
            _MetaInfoClassMember('common', REFERENCE_CLASS, 'Common' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.Common', 
                [], [], 
                '''                generic routing policy framework and
                configuration parameters
                ''',
                'common',
                'model-structure', False),
            _MetaInfoClassMember('igp-policy', REFERENCE_CLASS, 'IgpPolicy' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.IgpPolicy', 
                [], [], 
                '''                IGP routing policy knobs -- may include
                policy parameters for specific IGPs
                ''',
                'igp_policy',
                'model-structure', False),
            _MetaInfoClassMember('vrf-policy', REFERENCE_CLASS, 'VrfPolicy' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.VrfPolicy', 
                [], [], 
                '''                import/export policies for VRFs
                ''',
                'vrf_policy',
                'model-structure', False),
            ],
            'model-structure',
            'routing-policy',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bfd' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bfd',
            False, 
            [
            ],
            'model-structure',
            'bfd',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bgp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bgp',
            False, 
            [
            ],
            'model-structure',
            'bgp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igmp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igmp',
            False, 
            [
            ],
            'model-structure',
            'igmp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IgpCommon' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IgpCommon',
            False, 
            [
            ],
            'model-structure',
            'igp-common',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IsIs' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IsIs',
            False, 
            [
            ],
            'model-structure',
            'is-is',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf2' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf2',
            False, 
            [
            ],
            'model-structure',
            'ospf2',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf3' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf3',
            False, 
            [
            ],
            'model-structure',
            'ospf3',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf',
            False, 
            [
            _MetaInfoClassMember('ospf2', REFERENCE_CLASS, 'Ospf2' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf2', 
                [], [], 
                '''                OSPF v2
                ''',
                'ospf2',
                'model-structure', False),
            _MetaInfoClassMember('ospf3', REFERENCE_CLASS, 'Ospf3' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf3', 
                [], [], 
                '''                OSPF v3
                ''',
                'ospf3',
                'model-structure', False),
            ],
            'model-structure',
            'ospf',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp',
            False, 
            [
            _MetaInfoClassMember('igp-common', REFERENCE_CLASS, 'IgpCommon' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IgpCommon', 
                [], [], 
                '''                Common parameters for IGP protocols
                ''',
                'igp_common',
                'model-structure', False),
            _MetaInfoClassMember('is-is', REFERENCE_CLASS, 'IsIs' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IsIs', 
                [], [], 
                '''                IS-IS IGP routing protocol
                ''',
                'is_is',
                'model-structure', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf', 
                [], [], 
                '''                OSPF IGP routing protocols
                ''',
                'ospf',
                'model-structure', False),
            ],
            'model-structure',
            'igp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Pim' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Pim',
            False, 
            [
            ],
            'model-structure',
            'pim',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.StaticRoutes' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.StaticRoutes',
            False, 
            [
            ],
            'model-structure',
            'static-routes',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name or id of the routing instance / VRF
                ''',
                'vrf_name',
                'model-structure', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bfd', 
                [], [], 
                '''                bidirectional forwarding detection
                ''',
                'bfd',
                'model-structure', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bgp', 
                [], [], 
                '''                BGP 4
                ''',
                'bgp',
                'model-structure', False),
            _MetaInfoClassMember('igmp', REFERENCE_CLASS, 'Igmp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igmp', 
                [], [], 
                '''                Internet group management protocol
                ''',
                'igmp',
                'model-structure', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp', 
                [], [], 
                '''                interior gateway protocols
                ''',
                'igp',
                'model-structure', False),
            _MetaInfoClassMember('pim', REFERENCE_CLASS, 'Pim' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Pim', 
                [], [], 
                '''                protocol independent multicast
                ''',
                'pim',
                'model-structure', False),
            _MetaInfoClassMember('static-routes', REFERENCE_CLASS, 'StaticRoutes' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.StaticRoutes', 
                [], [], 
                '''                static route that are manually created
                ''',
                'static_routes',
                'model-structure', False),
            ],
            'model-structure',
            'vrf',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter.Layer3Protocols' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter.Layer3Protocols',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global', 
                [], [], 
                '''                router-wide instance of each routing protocol
                ''',
                'global_',
                'model-structure', False),
            _MetaInfoClassMember('routing-policy', REFERENCE_CLASS, 'RoutingPolicy' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy', 
                [], [], 
                '''                models related to routing policy across
                protocols and VRFs
                ''',
                'routing_policy',
                'model-structure', False),
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf', 
                [], [], 
                '''                list of VRF instances
                ''',
                'vrf',
                'model-structure', False),
            ],
            'model-structure',
            'layer-3-protocols',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters.LogicalRouter' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters.LogicalRouter',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                identifier of the logical router instance
                ''',
                'router_id',
                'model-structure', True),
            _MetaInfoClassMember('layer-2-protocols', REFERENCE_CLASS, 'Layer2Protocols' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer2Protocols', 
                [], [], 
                '''                layer 2 protocols and features
                ''',
                'layer_2_protocols',
                'model-structure', False),
            _MetaInfoClassMember('layer-3-protocols', REFERENCE_CLASS, 'Layer3Protocols' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter.Layer3Protocols', 
                [], [], 
                '''                layer 3 protocols and features
                ''',
                'layer_3_protocols',
                'model-structure', False),
            _MetaInfoClassMember('router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                identifier of the logical router instance
                ''',
                'router_name',
                'model-structure', False),
            ],
            'model-structure',
            'logical-router',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.LogicalRouters' : {
        'meta_info' : _MetaInfoClass('Device.LogicalRouters',
            False, 
            [
            _MetaInfoClassMember('logical-router', REFERENCE_LIST, 'LogicalRouter' , 'ydk.models.model.model_structure', 'Device.LogicalRouters.LogicalRouter', 
                [], [], 
                '''                list of logical router instances
                ''',
                'logical_router',
                'model-structure', False),
            ],
            'model-structure',
            'logical-routers',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.Qos' : {
        'meta_info' : _MetaInfoClass('Device.Qos',
            False, 
            [
            ],
            'model-structure',
            'qos',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Aaa.Radius' : {
        'meta_info' : _MetaInfoClass('Device.System.Aaa.Radius',
            False, 
            [
            ],
            'model-structure',
            'radius',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Aaa.Tacacs' : {
        'meta_info' : _MetaInfoClass('Device.System.Aaa.Tacacs',
            False, 
            [
            ],
            'model-structure',
            'tacacs',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Aaa' : {
        'meta_info' : _MetaInfoClass('Device.System.Aaa',
            False, 
            [
            _MetaInfoClassMember('radius', REFERENCE_CLASS, 'Radius' , 'ydk.models.model.model_structure', 'Device.System.Aaa.Radius', 
                [], [], 
                '''                RADIUS
                ''',
                'radius',
                'model-structure', False),
            _MetaInfoClassMember('tacacs', REFERENCE_CLASS, 'Tacacs' , 'ydk.models.model.model_structure', 'Device.System.Aaa.Tacacs', 
                [], [], 
                '''                TACACS+ configuration
                ''',
                'tacacs',
                'model-structure', False),
            ],
            'model-structure',
            'aaa',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Dhcp' : {
        'meta_info' : _MetaInfoClass('Device.System.Dhcp',
            False, 
            [
            ],
            'model-structure',
            'dhcp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Dns' : {
        'meta_info' : _MetaInfoClass('Device.System.Dns',
            False, 
            [
            ],
            'model-structure',
            'dns',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Ntp' : {
        'meta_info' : _MetaInfoClass('Device.System.Ntp',
            False, 
            [
            ],
            'model-structure',
            'ntp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Oam.Cfm' : {
        'meta_info' : _MetaInfoClass('Device.System.Oam.Cfm',
            False, 
            [
            ],
            'model-structure',
            'cfm',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Oam.Snmp' : {
        'meta_info' : _MetaInfoClass('Device.System.Oam.Snmp',
            False, 
            [
            ],
            'model-structure',
            'snmp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Oam.Twamp' : {
        'meta_info' : _MetaInfoClass('Device.System.Oam.Twamp',
            False, 
            [
            ],
            'model-structure',
            'twamp',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Oam' : {
        'meta_info' : _MetaInfoClass('Device.System.Oam',
            False, 
            [
            _MetaInfoClassMember('cfm', REFERENCE_CLASS, 'Cfm' , 'ydk.models.model.model_structure', 'Device.System.Oam.Cfm', 
                [], [], 
                '''                Ethernet connectivity fault management.  Also includes
                options that are associated with specific interfaces, such
                as maintenance endpoint domains.
                ''',
                'cfm',
                'model-structure', False),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp' , 'ydk.models.model.model_structure', 'Device.System.Oam.Snmp', 
                [], [], 
                '''                SNMP server information, e.g., allowed clients
                ''',
                'snmp',
                'model-structure', False),
            _MetaInfoClassMember('twamp', REFERENCE_CLASS, 'Twamp' , 'ydk.models.model.model_structure', 'Device.System.Oam.Twamp', 
                [], [], 
                '''                Two-way active measurement protocol for measuring
                round-trip IP layer performance.
                ''',
                'twamp',
                'model-structure', False),
            ],
            'model-structure',
            'oam',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Ssh' : {
        'meta_info' : _MetaInfoClass('Device.System.Ssh',
            False, 
            [
            ],
            'model-structure',
            'ssh',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.StatColl' : {
        'meta_info' : _MetaInfoClass('Device.System.StatColl',
            False, 
            [
            ],
            'model-structure',
            'stat-coll',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Syslog' : {
        'meta_info' : _MetaInfoClass('Device.System.Syslog',
            False, 
            [
            ],
            'model-structure',
            'syslog',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System.Users' : {
        'meta_info' : _MetaInfoClass('Device.System.Users',
            False, 
            [
            ],
            'model-structure',
            'users',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device.System' : {
        'meta_info' : _MetaInfoClass('Device.System',
            False, 
            [
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa' , 'ydk.models.model.model_structure', 'Device.System.Aaa', 
                [], [], 
                '''                authentication, authorization, and accounting
                ''',
                'aaa',
                'model-structure', False),
            _MetaInfoClassMember('dhcp', REFERENCE_CLASS, 'Dhcp' , 'ydk.models.model.model_structure', 'Device.System.Dhcp', 
                [], [], 
                '''                dhcp and relay services
                ''',
                'dhcp',
                'model-structure', False),
            _MetaInfoClassMember('dns', REFERENCE_CLASS, 'Dns' , 'ydk.models.model.model_structure', 'Device.System.Dns', 
                [], [], 
                '''                domain name service and resolver configurration
                ''',
                'dns',
                'model-structure', False),
            _MetaInfoClassMember('ntp', REFERENCE_CLASS, 'Ntp' , 'ydk.models.model.model_structure', 'Device.System.Ntp', 
                [], [], 
                '''                network time protocol configuration
                ''',
                'ntp',
                'model-structure', False),
            _MetaInfoClassMember('oam', REFERENCE_CLASS, 'Oam' , 'ydk.models.model.model_structure', 'Device.System.Oam', 
                [], [], 
                '''                commonly use OAM functions on devices
                ''',
                'oam',
                'model-structure', False),
            _MetaInfoClassMember('ssh', REFERENCE_CLASS, 'Ssh' , 'ydk.models.model.model_structure', 'Device.System.Ssh', 
                [], [], 
                '''                ssh server configuration
                ''',
                'ssh',
                'model-structure', False),
            _MetaInfoClassMember('stat-coll', REFERENCE_CLASS, 'StatColl' , 'ydk.models.model.model_structure', 'Device.System.StatColl', 
                [], [], 
                '''                mechanisms for data collection from devices, including
                packet and flow-level sampling
                ''',
                'stat_coll',
                'model-structure', False),
            _MetaInfoClassMember('syslog', REFERENCE_CLASS, 'Syslog' , 'ydk.models.model.model_structure', 'Device.System.Syslog', 
                [], [], 
                '''                syslog configuration
                ''',
                'syslog',
                'model-structure', False),
            _MetaInfoClassMember('users', REFERENCE_CLASS, 'Users' , 'ydk.models.model.model_structure', 'Device.System.Users', 
                [], [], 
                '''                local user configuration
                ''',
                'users',
                'model-structure', False),
            ],
            'model-structure',
            'system',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
    'Device' : {
        'meta_info' : _MetaInfoClass('Device',
            False, 
            [
            _MetaInfoClassMember('acl', REFERENCE_CLASS, 'Acl' , 'ydk.models.model.model_structure', 'Device.Acl', 
                [], [], 
                '''                ACLs and packet forwarding rules
                ''',
                'acl',
                'model-structure', False),
            _MetaInfoClassMember('hardware', REFERENCE_CLASS, 'Hardware' , 'ydk.models.model.model_structure', 'Device.Hardware', 
                [], [], 
                '''                This container is an anchor point for platform-specific
                configuration and operational state data.  It may be further
                organized into chassis, linecards, ports, etc.  It is
                expected that vendor or platform-specific augmentations
                would be used to populate this part of the device model
                ''',
                'hardware',
                'model-structure', False),
            _MetaInfoClassMember('info', REFERENCE_CLASS, 'Info' , 'ydk.models.model.model_structure', 'Device.Info', 
                [], [], 
                '''                This container is for base system information, including
                device type (e.g., physcal or virtual), model, serial no.,
                location, etc.
                ''',
                'info',
                'model-structure', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.model.model_structure', 'Device.Interfaces', 
                [], [], 
                '''                various interface models
                ''',
                'interfaces',
                'model-structure', False),
            _MetaInfoClassMember('logical-routers', REFERENCE_CLASS, 'LogicalRouters' , 'ydk.models.model.model_structure', 'Device.LogicalRouters', 
                [], [], 
                '''                devices may support multiple logical router
                instances
                ''',
                'logical_routers',
                'model-structure', False),
            _MetaInfoClassMember('qos', REFERENCE_CLASS, 'Qos' , 'ydk.models.model.model_structure', 'Device.Qos', 
                [], [], 
                '''                QoS, including policing, shaping, etc.
                ''',
                'qos',
                'model-structure', False),
            _MetaInfoClassMember('system', REFERENCE_CLASS, 'System' , 'ydk.models.model.model_structure', 'Device.System', 
                [], [], 
                '''                system services
                ''',
                'system',
                'model-structure', False),
            ],
            'model-structure',
            'device',
            _yang_ns._namespaces['model-structure'],
        'ydk.models.model.model_structure'
        ),
    },
}
_meta_table['Device.Interfaces.Addressing.Ipv4.Vrrp']['meta_info'].parent =_meta_table['Device.Interfaces.Addressing.Ipv4']['meta_info']
_meta_table['Device.Interfaces.Addressing.Ipv6.Vrrp']['meta_info'].parent =_meta_table['Device.Interfaces.Addressing.Ipv6']['meta_info']
_meta_table['Device.Interfaces.Addressing.Ipv4']['meta_info'].parent =_meta_table['Device.Interfaces.Addressing']['meta_info']
_meta_table['Device.Interfaces.Addressing.Ipv6']['meta_info'].parent =_meta_table['Device.Interfaces.Addressing']['meta_info']
_meta_table['Device.Interfaces.Ethernet.Aggregates']['meta_info'].parent =_meta_table['Device.Interfaces.Ethernet']['meta_info']
_meta_table['Device.Interfaces.Ethernet.Lfm']['meta_info'].parent =_meta_table['Device.Interfaces.Ethernet']['meta_info']
_meta_table['Device.Interfaces.Ethernet.Vlans']['meta_info'].parent =_meta_table['Device.Interfaces.Ethernet']['meta_info']
_meta_table['Device.Interfaces.Addressing']['meta_info'].parent =_meta_table['Device.Interfaces']['meta_info']
_meta_table['Device.Interfaces.Ethernet']['meta_info'].parent =_meta_table['Device.Interfaces']['meta_info']
_meta_table['Device.Interfaces.SonetSdh']['meta_info'].parent =_meta_table['Device.Interfaces']['meta_info']
_meta_table['Device.Interfaces.Tunnels']['meta_info'].parent =_meta_table['Device.Interfaces']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Arp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ipv6Ndp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Lldp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ptp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Rstp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Vsi']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf2']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf3']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IgpCommon']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IsIs']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.ConstrainedPath']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.IgpCongruent']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.Static']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Ldp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Rsvp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.SegmentRouting']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Global']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bfd']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bgp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igmp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Pim']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.StaticRoutes']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.BgpPolicy']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.Common']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.IgpPolicy']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.VrfPolicy']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf2']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf3']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IgpCommon']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IsIs']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bfd']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bgp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igmp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Pim']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.StaticRoutes']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols']['meta_info'].parent =_meta_table['Device.LogicalRouters.LogicalRouter']['meta_info']
_meta_table['Device.LogicalRouters.LogicalRouter']['meta_info'].parent =_meta_table['Device.LogicalRouters']['meta_info']
_meta_table['Device.System.Aaa.Radius']['meta_info'].parent =_meta_table['Device.System.Aaa']['meta_info']
_meta_table['Device.System.Aaa.Tacacs']['meta_info'].parent =_meta_table['Device.System.Aaa']['meta_info']
_meta_table['Device.System.Oam.Cfm']['meta_info'].parent =_meta_table['Device.System.Oam']['meta_info']
_meta_table['Device.System.Oam.Snmp']['meta_info'].parent =_meta_table['Device.System.Oam']['meta_info']
_meta_table['Device.System.Oam.Twamp']['meta_info'].parent =_meta_table['Device.System.Oam']['meta_info']
_meta_table['Device.System.Aaa']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.System.Dhcp']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.System.Dns']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.System.Ntp']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.System.Oam']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.System.Ssh']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.System.StatColl']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.System.Syslog']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.System.Users']['meta_info'].parent =_meta_table['Device.System']['meta_info']
_meta_table['Device.Acl']['meta_info'].parent =_meta_table['Device']['meta_info']
_meta_table['Device.Hardware']['meta_info'].parent =_meta_table['Device']['meta_info']
_meta_table['Device.Info']['meta_info'].parent =_meta_table['Device']['meta_info']
_meta_table['Device.Interfaces']['meta_info'].parent =_meta_table['Device']['meta_info']
_meta_table['Device.LogicalRouters']['meta_info'].parent =_meta_table['Device']['meta_info']
_meta_table['Device.Qos']['meta_info'].parent =_meta_table['Device']['meta_info']
_meta_table['Device.System']['meta_info'].parent =_meta_table['Device']['meta_info']
