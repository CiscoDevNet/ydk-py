""" CISCO_CBP_TC_MIB 

This MIB module defines textual conventions used by the
CISCO\-CBP\-BASE\-CFG\-MIB, CISCO\-CBP\-BASE\-MON\-MIB, and any MIB
modules extending these MIB modules.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CbpexecutionstrategyEnum(Enum):
    """
    CbpexecutionstrategyEnum

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

    other = 1

    doUntilSuccess = 2

    doUntilFailure = 3

    doAll = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CBP_TC_MIB as meta
        return meta._meta_table['CbpexecutionstrategyEnum']



