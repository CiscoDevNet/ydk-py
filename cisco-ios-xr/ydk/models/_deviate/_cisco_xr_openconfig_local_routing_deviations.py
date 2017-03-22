
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'LocalRoutes.LocalAggregates.Aggregate' : {
        'deviation_typ' : 'not_supported',
    },
    'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config.recurse' : {
        'deviation_typ' : 'not_supported',
    },
    'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State.recurse' : {
        'deviation_typ' : 'not_supported',
    },
}
