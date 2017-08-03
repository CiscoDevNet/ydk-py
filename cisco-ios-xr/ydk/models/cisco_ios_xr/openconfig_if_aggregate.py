""" openconfig_if_aggregate 

Model for managing aggregated (aka bundle, LAG) interfaces.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AggregationType(Enum):
    """
    AggregationType

    Type to define the lag\-type, i.e., how the LAG is

    defined and managed

    .. data:: LACP = 0

    	LAG managed by LACP

    .. data:: STATIC = 1

    	Statically configured bundle / LAG

    """

    LACP = Enum.YLeaf(0, "LACP")

    STATIC = Enum.YLeaf(1, "STATIC")



