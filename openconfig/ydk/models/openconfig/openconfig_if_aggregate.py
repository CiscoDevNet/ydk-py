""" openconfig_if_aggregate 

Model for managing aggregated (aka bundle, LAG) interfaces.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AggregationType(Enum):
    """
    AggregationType (Enum Class)

    Type to define the lag\-type, i.e., how the LAG is

    defined and managed

    .. data:: LACP = 0

    	LAG managed by LACP

    .. data:: STATIC = 1

    	Statically configured bundle / LAG

    """

    LACP = Enum.YLeaf(0, "LACP")

    STATIC = Enum.YLeaf(1, "STATIC")



