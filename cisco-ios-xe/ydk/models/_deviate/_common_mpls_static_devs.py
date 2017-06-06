
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'MplsStatic.MplsStaticCfg.InLabelLsps' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Interfaces' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.auto_next_hops' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('max_elements', 1),
        ]
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.NextHopType.address_type.layer2' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.NextHopType.address_type.layer3_ipv6' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.NextHopType.address_type.unnumberd' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.NextHopType.out_interface_name' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.Operations.operation.pop_and_forward' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.Operations.operation.preserve_stack' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.Operations.operation.push_label_stack' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.Operations.operation.swap_with_label_stack.Swap.Stack.label_stack' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('max_elements', 1),
        ]
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.resolution.explicit_next_hops.NextHop.protected_by' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.name' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps' : {
        'deviation_typ' : 'not_supported',
    },
    'MplsStatic.MplsStaticCfg.NamedLsps' : {
        'deviation_typ' : 'not_supported',
    },
}
