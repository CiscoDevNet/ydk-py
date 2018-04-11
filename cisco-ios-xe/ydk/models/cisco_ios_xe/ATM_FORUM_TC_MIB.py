""" ATM_FORUM_TC_MIB 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AtmServiceCategory(Enum):
    """
    AtmServiceCategory (Enum Class)

    ATM Service Categories use this data type

    .. data:: other = 1

    .. data:: cbr = 2

    .. data:: rtVbr = 3

    .. data:: nrtVbr = 4

    .. data:: abr = 5

    .. data:: ubr = 6

    """

    other = Enum.YLeaf(1, "other")

    cbr = Enum.YLeaf(2, "cbr")

    rtVbr = Enum.YLeaf(3, "rtVbr")

    nrtVbr = Enum.YLeaf(4, "nrtVbr")

    abr = Enum.YLeaf(5, "abr")

    ubr = Enum.YLeaf(6, "ubr")


class TruthValue(Enum):
    """
    TruthValue (Enum Class)

    Boolean values use this data type from RFC\-1903

    .. data:: true = 1

    .. data:: false = 2

    """

    true = Enum.YLeaf(1, "true")

    false = Enum.YLeaf(2, "false")



