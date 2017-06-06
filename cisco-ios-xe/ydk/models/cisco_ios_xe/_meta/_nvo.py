


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'OverlayEncapTypeIdentity' : {
        'meta_info' : _MetaInfoClass('OverlayEncapTypeIdentity',
            False, 
            [
            ],
            'nvo',
            'overlay-encap-type',
            _yang_ns._namespaces['nvo'],
        'ydk.models.cisco_ios_xe.nvo'
        ),
    },
    'NvoInstances.NvoInstance.VirtualNetwork.Multicast' : {
        'meta_info' : _MetaInfoClass('NvoInstances.NvoInstance.VirtualNetwork.Multicast',
            False, 
            [
            _MetaInfoClassMember('multicast-group-max', ATTRIBUTE, 'str' , None, None, 
                [], [b'(2((2[4-9])|(3[0-9]))\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                End of IPV4 Multicast group 
                address (leave unspecified for single value
                ''',
                'multicast_group_max',
                'nvo', False),
            _MetaInfoClassMember('multicast-group-min', ATTRIBUTE, 'str' , None, None, 
                [], [b'(2((2[4-9])|(3[0-9]))\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                Single IPV4 Multicast group 
                address or start of range
                ''',
                'multicast_group_min',
                'nvo', False),
            ],
            'nvo',
            'multicast',
            _yang_ns._namespaces['nvo'],
        'ydk.models.cisco_ios_xe.nvo'
        ),
    },
    'NvoInstances.NvoInstance.VirtualNetwork.Peers' : {
        'meta_info' : _MetaInfoClass('NvoInstances.NvoInstance.VirtualNetwork.Peers',
            False, 
            [
            _MetaInfoClassMember('peer-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                VTEP peer IP address
                ''',
                'peer_ip',
                'nvo', True, [
                    _MetaInfoClassMember('peer-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VTEP peer IP address
                        ''',
                        'peer_ip',
                        'nvo', True),
                    _MetaInfoClassMember('peer-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        VTEP peer IP address
                        ''',
                        'peer_ip',
                        'nvo', True),
                ]),
            ],
            'nvo',
            'peers',
            _yang_ns._namespaces['nvo'],
        'ydk.models.cisco_ios_xe.nvo'
        ),
    },
    'NvoInstances.NvoInstance.VirtualNetwork.EndHostDiscoveryEnum' : _MetaInfoEnum('EndHostDiscoveryEnum', 'ydk.models.cisco_ios_xe.nvo',
        {
            'flood-and-learn':'flood_and_learn',
            'bgp':'bgp',
        }, 'nvo', _yang_ns._namespaces['nvo']),
    'NvoInstances.NvoInstance.VirtualNetwork' : {
        'meta_info' : _MetaInfoClass('NvoInstances.NvoInstance.VirtualNetwork',
            False, 
            [
            _MetaInfoClassMember('vni-start', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Single Virtual Network Identifier 
                or start of range
                ''',
                'vni_start',
                'nvo', True),
            _MetaInfoClassMember('vni-end', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                End of Virtual Network Identifier range 
                (make equal to vni-start for single vni
                ''',
                'vni_end',
                'nvo', True),
            _MetaInfoClassMember('bgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use control protocol BGP to discover 
                peers
                ''',
                'bgp',
                'nvo', False),
            _MetaInfoClassMember('end-host-discovery', REFERENCE_ENUM_CLASS, 'EndHostDiscoveryEnum' , 'ydk.models.cisco_ios_xe.nvo', 'NvoInstances.NvoInstance.VirtualNetwork.EndHostDiscoveryEnum', 
                [], [], 
                '''                How to peform endpoint discovery
                ''',
                'end_host_discovery',
                'nvo', False),
            _MetaInfoClassMember('multicast', REFERENCE_CLASS, 'Multicast' , 'ydk.models.cisco_ios_xe.nvo', 'NvoInstances.NvoInstance.VirtualNetwork.Multicast', 
                [], [], 
                '''                Mulitcast group range associated 
                with the VxLAN segment(s)
                ''',
                'multicast',
                'nvo', False),
            _MetaInfoClassMember('peers', REFERENCE_LIST, 'Peers' , 'ydk.models.cisco_ios_xe.nvo', 'NvoInstances.NvoInstance.VirtualNetwork.Peers', 
                [], [], 
                '''                List of VTEP peers
                ''',
                'peers',
                'nvo', False),
            _MetaInfoClassMember('routing-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'routing_instance',
                'nvo', False),
            _MetaInfoClassMember('suppress-arp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ARP request suppression for this VNI
                ''',
                'suppress_arp',
                'nvo', False),
            ],
            'nvo',
            'virtual-network',
            _yang_ns._namespaces['nvo'],
        'ydk.models.cisco_ios_xe.nvo'
        ),
    },
    'NvoInstances.NvoInstance' : {
        'meta_info' : _MetaInfoClass('NvoInstances.NvoInstance',
            False, 
            [
            _MetaInfoClassMember('nvo-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Network Virtualization Overlay Instance 
                Identifier
                ''',
                'nvo_id',
                'nvo', True),
            _MetaInfoClassMember('overlay-encapsulation', REFERENCE_IDENTITY_CLASS, 'OverlayEncapTypeIdentity' , 'ydk.models.cisco_ios_xe.nvo', 'OverlayEncapTypeIdentity', 
                [], [], 
                '''                Encapsulation type
                ''',
                'overlay_encapsulation',
                'nvo', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source interface name
                ''',
                'source_interface',
                'nvo', False),
            _MetaInfoClassMember('virtual-network', REFERENCE_LIST, 'VirtualNetwork' , 'ydk.models.cisco_ios_xe.nvo', 'NvoInstances.NvoInstance.VirtualNetwork', 
                [], [], 
                '''                VNI member attributes
                ''',
                'virtual_network',
                'nvo', False),
            ],
            'nvo',
            'nvo-instance',
            _yang_ns._namespaces['nvo'],
        'ydk.models.cisco_ios_xe.nvo'
        ),
    },
    'NvoInstances' : {
        'meta_info' : _MetaInfoClass('NvoInstances',
            False, 
            [
            _MetaInfoClassMember('nvo-instance', REFERENCE_LIST, 'NvoInstance' , 'ydk.models.cisco_ios_xe.nvo', 'NvoInstances.NvoInstance', 
                [], [], 
                '''                List of instances
                ''',
                'nvo_instance',
                'nvo', False),
            ],
            'nvo',
            'nvo-instances',
            _yang_ns._namespaces['nvo'],
        'ydk.models.cisco_ios_xe.nvo'
        ),
    },
    'NvgreTypeIdentity' : {
        'meta_info' : _MetaInfoClass('NvgreTypeIdentity',
            False, 
            [
            ],
            'nvo',
            'nvgre-type',
            _yang_ns._namespaces['nvo'],
        'ydk.models.cisco_ios_xe.nvo'
        ),
    },
    'VxlanTypeIdentity' : {
        'meta_info' : _MetaInfoClass('VxlanTypeIdentity',
            False, 
            [
            ],
            'nvo',
            'vxlan-type',
            _yang_ns._namespaces['nvo'],
        'ydk.models.cisco_ios_xe.nvo'
        ),
    },
}
_meta_table['NvoInstances.NvoInstance.VirtualNetwork.Multicast']['meta_info'].parent =_meta_table['NvoInstances.NvoInstance.VirtualNetwork']['meta_info']
_meta_table['NvoInstances.NvoInstance.VirtualNetwork.Peers']['meta_info'].parent =_meta_table['NvoInstances.NvoInstance.VirtualNetwork']['meta_info']
_meta_table['NvoInstances.NvoInstance.VirtualNetwork']['meta_info'].parent =_meta_table['NvoInstances.NvoInstance']['meta_info']
_meta_table['NvoInstances.NvoInstance']['meta_info'].parent =_meta_table['NvoInstances']['meta_info']
