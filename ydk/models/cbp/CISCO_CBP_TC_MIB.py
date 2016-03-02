""" CISCO_CBP_TC_MIB 

This MIB module defines textual conventions used by the
CISCO\-CBP\-BASE\-CFG\-MIB, CISCO\-CBP\-BASE\-MON\-MIB, and any MIB
modules extending these MIB modules.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CbpExecutionStrategy_Enum(Enum):
    """
    CbpExecutionStrategy_Enum

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

    """

    OTHER = 1

    DOUNTILSUCCESS = 2

    DOUNTILFAILURE = 3

    DOALL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cbp._meta import _CISCO_CBP_TC_MIB as meta
        return meta._meta_table['CbpExecutionStrategy_Enum']



