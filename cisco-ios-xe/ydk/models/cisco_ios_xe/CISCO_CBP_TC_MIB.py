""" CISCO_CBP_TC_MIB 

This MIB module defines textual conventions used by the
CISCO\-CBP\-BASE\-CFG\-MIB, CISCO\-CBP\-BASE\-MON\-MIB, and any MIB
modules extending these MIB modules.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cbpexecutionstrategy(Enum):
    """
    Cbpexecutionstrategy

    An enumerated integer\-value describing how to execute an

    ordered set of actions\:

        'other'

            The implementation of the MIB using this textual

            convention does not recognize the specified execution

            strategy.

        'doUntilSuccess'

            The system sequentially executes the actions in the

            set until one succeeds.

        'doUntilFailure'

            The system sequentially executes the actions in the

            set until one fails.

        'doAll'

            The system sequentially executes all actions in the set,

            regardless of whether they succeed or fail.

    .. data:: other = 1

    .. data:: doUntilSuccess = 2

    .. data:: doUntilFailure = 3

    .. data:: doAll = 4

    """

    other = Enum.YLeaf(1, "other")

    doUntilSuccess = Enum.YLeaf(2, "doUntilSuccess")

    doUntilFailure = Enum.YLeaf(3, "doUntilFailure")

    doAll = Enum.YLeaf(4, "doAll")



