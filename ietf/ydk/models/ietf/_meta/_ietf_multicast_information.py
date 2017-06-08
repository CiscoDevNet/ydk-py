


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'VirtualTypeEnum' : _MetaInfoEnum('VirtualTypeEnum', 'ydk.models.ietf.ietf_multicast_information',
        {
            'vxlan':'vxlan',
            'virtual subnet':'virtual_subnet',
            'vni':'vni',
        }, 'ietf-multicast-information', _yang_ns._namespaces['ietf-multicast-information']),
    'MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation.EgressNodes' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation.EgressNodes',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of egress nodes.
                ''',
                'number',
                'ietf-multicast-information', True),
            _MetaInfoClassMember('egress-node', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The egress multicast nodes of multicast flow.
                Or the egress node of MVPN and BIER. In MVPN, this is the
                address of egress PE; in BIER, this is the BFR-prefix of
                ingress nodes.
                ''',
                'egress_node',
                'ietf-multicast-information', False, [
                    _MetaInfoClassMember('egress-node', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The egress multicast nodes of multicast flow.
                        Or the egress node of MVPN and BIER. In MVPN, this is the
                        address of egress PE; in BIER, this is the BFR-prefix of
                        ingress nodes.
                        ''',
                        'egress_node',
                        'ietf-multicast-information', False),
                    _MetaInfoClassMember('egress-node', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The egress multicast nodes of multicast flow.
                        Or the egress node of MVPN and BIER. In MVPN, this is the
                        address of egress PE; in BIER, this is the BFR-prefix of
                        ingress nodes.
                        ''',
                        'egress_node',
                        'ietf-multicast-information', False),
                ]),
            ],
            'ietf-multicast-information',
            'egress-nodes',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation',
            False, 
            [
            _MetaInfoClassMember('egress-nodes', REFERENCE_LIST, 'EgressNodes' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation.EgressNodes', 
                [], [], 
                '''                This ID information of one adjacency.
                ''',
                'egress_nodes',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('ingress-node', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The ingress node of multicast flow. Or the ingress
                node of MVPN and BIER. In MVPN, this is the address of ingress
                PE; in BIER, this is the BFR-prefix of ingress nodes.
                ''',
                'ingress_node',
                'ietf-multicast-information', False, [
                    _MetaInfoClassMember('ingress-node', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The ingress node of multicast flow. Or the ingress
                        node of MVPN and BIER. In MVPN, this is the address of ingress
                        PE; in BIER, this is the BFR-prefix of ingress nodes.
                        ''',
                        'ingress_node',
                        'ietf-multicast-information', False),
                    _MetaInfoClassMember('ingress-node', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The ingress node of multicast flow. Or the ingress
                        node of MVPN and BIER. In MVPN, this is the address of ingress
                        PE; in BIER, this is the BFR-prefix of ingress nodes.
                        ''',
                        'ingress_node',
                        'ietf-multicast-information', False),
                ]),
            ],
            'ietf-multicast-information',
            'nodes-information',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation.EgressNodes' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation.EgressNodes',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of egress nodes.
                ''',
                'number',
                'ietf-multicast-information', True),
            _MetaInfoClassMember('egress-node', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The egress multicast nodes of multicast flow.
                This is the BFR-id of egress nodes.
                ''',
                'egress_node',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'egress-nodes',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation',
            False, 
            [
            _MetaInfoClassMember('egress-nodes', REFERENCE_LIST, 'EgressNodes' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation.EgressNodes', 
                [], [], 
                '''                This ID information of one adjacency.
                ''',
                'egress_nodes',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('ingress-node', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The ingress node of multicast flow. This is the
                BFR-id of ingress nodes.
                ''',
                'ingress_node',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('sub-domain', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The sub-domain that this multicast flow belongs to.
                ''',
                'sub_domain',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'bier-information',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastOverlay.OverlayTechnology' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastOverlay.OverlayTechnology',
            False, 
            [
            ],
            'ietf-multicast-information',
            'overlay-technology',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastOverlay' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastOverlay',
            False, 
            [
            _MetaInfoClassMember('bier-information', REFERENCE_CLASS, 'BierInformation' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation', 
                [], [], 
                '''                The ingress and egress BIER nodes information.
                ''',
                'bier_information',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('nodes-information', REFERENCE_CLASS, 'NodesInformation' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation', 
                [], [], 
                '''                The ingress and egress nodes information.
                ''',
                'nodes_information',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('overlay-technology', REFERENCE_CLASS, 'OverlayTechnology' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastOverlay.OverlayTechnology', 
                [], [], 
                '''                The possible overlay technologies for multicast service.
                ''',
                'overlay_technology',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'multicast-overlay',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastTransport.Bier' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastTransport.Bier',
            False, 
            [
            _MetaInfoClassMember('bitstringlength', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The bitstringlength used by BIER forwarding.
                ''',
                'bitstringlength',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('ecmp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The capability of ECMP.
                ''',
                'ecmp',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('frr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The capability of fast re-route.
                ''',
                'frr',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('set-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The set identifier used by this multicast flow, especially in BIER TE.
                ''',
                'set_identifier',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('sub-domain', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The subdomain id that this multicast flow belongs to.
                ''',
                'sub_domain',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'bier',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastTransport.CiscoMode' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastTransport.CiscoMode',
            False, 
            [
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the bfd function should be supported.
                ''',
                'bfd',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the graceful restart function should be supported.
                ''',
                'graceful_restart',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('p-group', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The address of p-group.
                ''',
                'p_group',
                'ietf-multicast-information', False, [
                    _MetaInfoClassMember('p-group', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The address of p-group.
                        ''',
                        'p_group',
                        'ietf-multicast-information', False),
                    _MetaInfoClassMember('p-group', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The address of p-group.
                        ''',
                        'p_group',
                        'ietf-multicast-information', False),
                ]),
            ],
            'ietf-multicast-information',
            'cisco-mode',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastTransport.Mpls' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastTransport.Mpls',
            False, 
            [
            _MetaInfoClassMember('mldp-backup-tunnel', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the backup tunnel function should be supported.
                ''',
                'mldp_backup_tunnel',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('mldp-frr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the fast re-route function should be supported.
                ''',
                'mldp_frr',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('mldp-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The tunnel id that correspond this flow.
                ''',
                'mldp_tunnel_id',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('te-backup-tunnel', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the backup tunnel function should be supported.
                ''',
                'te_backup_tunnel',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('te-frr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the fast re-route function should be supported.
                ''',
                'te_frr',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('te-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The tunnel id that correspond this flow.
                ''',
                'te_tunnel_id',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'mpls',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastTransport.Pim' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastTransport.Pim',
            False, 
            [
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the bfd function should be supported.
                ''',
                'bfd',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the graceful restart function should be supported.
                ''',
                'graceful_restart',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'pim',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastTransport' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastTransport',
            False, 
            [
            _MetaInfoClassMember('bier', REFERENCE_CLASS, 'Bier' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastTransport.Bier', 
                [], [], 
                '''                The transport technology is BIER.
                ''',
                'bier',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('cisco-mode', REFERENCE_CLASS, 'CiscoMode' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastTransport.CiscoMode', 
                [], [], 
                '''                The transport technology is cisco-mode.
                ''',
                'cisco_mode',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastTransport.Mpls', 
                [], [], 
                '''                The transport technology is mpls.
                ''',
                'mpls',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('pim', REFERENCE_CLASS, 'Pim' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastTransport.Pim', 
                [], [], 
                '''                The transport technology is PIM.
                ''',
                'pim',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'multicast-transport',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastUnderlay.Bgp' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastUnderlay.Bgp',
            False, 
            [
            ],
            'ietf-multicast-information',
            'bgp',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastUnderlay.Ospf' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastUnderlay.Ospf',
            False, 
            [
            _MetaInfoClassMember('topology-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The topology id of ospf instance.
                ''',
                'topology_id',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'ospf',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastUnderlay.Isis' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastUnderlay.Isis',
            False, 
            [
            _MetaInfoClassMember('topology-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The topology id of isis instance.
                ''',
                'topology_id',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'isis',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastUnderlay.Babel' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastUnderlay.Babel',
            False, 
            [
            ],
            'ietf-multicast-information',
            'babel',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastUnderlay.Pim' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastUnderlay.Pim',
            False, 
            [
            ],
            'ietf-multicast-information',
            'pim',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo.MulticastUnderlay' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo.MulticastUnderlay',
            False, 
            [
            _MetaInfoClassMember('babel', REFERENCE_CLASS, 'Babel' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastUnderlay.Babel', 
                [], [], 
                '''                The underlay technology is Babel.
                ''',
                'babel',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastUnderlay.Bgp', 
                [], [], 
                '''                The underlay technology is BGP.
                ''',
                'bgp',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastUnderlay.Isis', 
                [], [], 
                '''                The underlay technology is ISIS.
                ''',
                'isis',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastUnderlay.Ospf', 
                [], [], 
                '''                The underlay technology is OSPF.
                ''',
                'ospf',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('pim', REFERENCE_CLASS, 'Pim' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastUnderlay.Pim', 
                [], [], 
                '''                The underlay technology is PIM.
                ''',
                'pim',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('underlay-requirement', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the underlay technology should be required.
                ''',
                'underlay_requirement',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'multicast-underlay',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation.MulticastInfo' : {
        'meta_info' : _MetaInfoClass('MulticastInformation.MulticastInfo',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The address of multicast group.
                ''',
                'group_address',
                'ietf-multicast-information', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The address of multicast group.
                        ''',
                        'group_address',
                        'ietf-multicast-information', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The address of multicast group.
                        ''',
                        'group_address',
                        'ietf-multicast-information', True),
                ]),
            _MetaInfoClassMember('group-wildcard', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The wildcard information of group.
                ''',
                'group_wildcard',
                'ietf-multicast-information', True),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The address of multicast source. The value set to zero
                means that the receiver interests in all source that relevant to
                one group.
                ''',
                'source_address',
                'ietf-multicast-information', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The address of multicast source. The value set to zero
                        means that the receiver interests in all source that relevant to
                        one group.
                        ''',
                        'source_address',
                        'ietf-multicast-information', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The address of multicast source. The value set to zero
                        means that the receiver interests in all source that relevant to
                        one group.
                        ''',
                        'source_address',
                        'ietf-multicast-information', True),
                ]),
            _MetaInfoClassMember('source-wildcard', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The wildcard information of source.
                ''',
                'source_wildcard',
                'ietf-multicast-information', True),
            _MetaInfoClassMember('vni-type', REFERENCE_ENUM_CLASS, 'VirtualTypeEnum' , 'ydk.models.ietf.ietf_multicast_information', 'VirtualTypeEnum', 
                [], [], 
                '''                The type of virtual network identifier. Include the Vxlan
                NVGRE and Geneve.
                ''',
                'vni_type',
                'ietf-multicast-information', True),
            _MetaInfoClassMember('vni-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of Vxlan network identifier, virtual subnet ID
                or virtual net identifier.
                ''',
                'vni_value',
                'ietf-multicast-information', True),
            _MetaInfoClassMember('vpn-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The vpn-id of the multicast flow.
                If there is global instance, the vpnid value should be zero.
                ''',
                'vpn_id',
                'ietf-multicast-information', True),
            _MetaInfoClassMember('multicast-overlay', REFERENCE_CLASS, 'MulticastOverlay' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastOverlay', 
                [], [], 
                '''                The overlay information of multicast service.
                ''',
                'multicast_overlay',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('multicast-transport', REFERENCE_CLASS, 'MulticastTransport' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastTransport', 
                [], [], 
                '''                The transportion of multicast service.
                ''',
                'multicast_transport',
                'ietf-multicast-information', False),
            _MetaInfoClassMember('multicast-underlay', REFERENCE_CLASS, 'MulticastUnderlay' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo.MulticastUnderlay', 
                [], [], 
                '''                The underlay of multicast service.
                ''',
                'multicast_underlay',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'multicast-info',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
    'MulticastInformation' : {
        'meta_info' : _MetaInfoClass('MulticastInformation',
            False, 
            [
            _MetaInfoClassMember('multicast-info', REFERENCE_LIST, 'MulticastInfo' , 'ydk.models.ietf.ietf_multicast_information', 'MulticastInformation.MulticastInfo', 
                [], [], 
                '''                The detail multicast information.
                ''',
                'multicast_info',
                'ietf-multicast-information', False),
            ],
            'ietf-multicast-information',
            'multicast-information',
            _yang_ns._namespaces['ietf-multicast-information'],
        'ydk.models.ietf.ietf_multicast_information'
        ),
    },
}
_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation.EgressNodes']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation.EgressNodes']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.NodesInformation']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.BierInformation']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay.OverlayTechnology']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastTransport.Bier']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastTransport']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastTransport.CiscoMode']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastTransport']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastTransport.Mpls']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastTransport']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastTransport.Pim']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastTransport']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Bgp']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Ospf']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Isis']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Babel']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay.Pim']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastOverlay']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastTransport']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo']['meta_info']
_meta_table['MulticastInformation.MulticastInfo.MulticastUnderlay']['meta_info'].parent =_meta_table['MulticastInformation.MulticastInfo']['meta_info']
_meta_table['MulticastInformation.MulticastInfo']['meta_info'].parent =_meta_table['MulticastInformation']['meta_info']
