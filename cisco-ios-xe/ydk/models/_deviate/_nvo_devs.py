
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'NvoInstances.NvoInstance.VirtualNetwork.end_host_discovery' : {
        'deviation_typ' : 'not_supported',
    },
    'NvoInstances.NvoInstance.VirtualNetwork.replication_mode.bgp' : {
        'deviation_typ' : 'not_supported',
    },
    'NvoInstances.NvoInstance.VirtualNetwork.replication_mode.static_peer_list' : {
        'deviation_typ' : 'not_supported',
    },
    'NvoInstances.NvoInstance.VirtualNetwork.routing_instance' : {
        'deviation_typ' : 'not_supported',
    },
    'NvoInstances.NvoInstance.VirtualNetwork.suppress_arp' : {
        'deviation_typ' : 'not_supported',
    },
    'NvoInstances.NvoInstance.overlay_encapsulation' : {
        'deviation_typ' : 'not_supported',
    },
}
