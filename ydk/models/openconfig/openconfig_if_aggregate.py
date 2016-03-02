""" openconfig_if_aggregate 

Model for managing aggregated interfaces, including LACP\-
managed aggregates

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AggregationType_Enum(Enum):
    """
    AggregationType_Enum

    Type to define the lag\-type, i.e., how the LAG is
    defined and managed

    """

    """

    LAG managed by LACP

    """
    LACP = 0

    """

    Statically configured bundle / LAG

    """
    STATIC = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['AggregationType_Enum']


class LacpActivityType_Enum(Enum):
    """
    LacpActivityType_Enum

    Describes the LACP membership type, active or passive, of the
    interface in the aggregate

    """

    """

    Interface is an active member, i.e., will detect and
    maintain aggregates

    """
    ACTIVE = 0

    """

    Interface is a passive member, i.e., it participates
    with an active partner

    """
    PASSIVE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['LacpActivityType_Enum']


class LacpPeriodType_Enum(Enum):
    """
    LacpPeriodType_Enum

    Defines the period options for the time between sending
    LACP messages

    """

    """

    Send LACP packets every second

    """
    FAST = 0

    """

    Send LACP packets every 30 seconds

    """
    SLOW = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['LacpPeriodType_Enum']


class LacpSynchronizationType_Enum(Enum):
    """
    LacpSynchronizationType_Enum

    Indicates LACP synchronization state of participant

    """

    """

    Participant is in sync with the system id and key
    transmitted

    """
    IN_SYNC = 0

    """

    Participant is not in sync with the system id and key
    transmitted

    """
    OUT_SYNC = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['LacpSynchronizationType_Enum']


class LacpTimeoutType_Enum(Enum):
    """
    LacpTimeoutType_Enum

    Type of timeout used, short or long, by LACP participants

    """

    """

    Participant wishes to use long timeouts to detect
    status of the aggregate, i.e., will expect less frequent
    transmissions. Long timeout is 90 seconds.

    """
    LONG = 0

    """

    Participant wishes to use short timeouts, i.e., expects
    frequent transmissions to aggressively detect status
    changes. Short timeout is 3 seconds.

    """
    SHORT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['LacpTimeoutType_Enum']



