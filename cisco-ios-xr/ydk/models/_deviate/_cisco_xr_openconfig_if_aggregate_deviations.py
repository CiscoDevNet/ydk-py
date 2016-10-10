
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Interfaces.Interface.Aggregation.Config.lag_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Aggregation.Lacp.Config.interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Aggregation.Lacp.Config.lacp_mode' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Aggregation.Lacp.Members.Member.State.Counters.lacp_tx_errors' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Aggregation.Lacp.State.interval' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Aggregation.Lacp.State.lacp_mode' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Aggregation.State.lag_type' : {
        'deviation_typ' : 'not_supported',
    },
    'Interfaces.Interface.Aggregation.State.members' : {
        'deviation_typ' : 'not_supported',
    },
}
