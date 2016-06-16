""" openconfig_if_aggregate 

Model for managing aggregated interfaces, including LACP\-
managed aggregates

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AggregationTypeEnum(Enum):
    """
    AggregationTypeEnum

    Type to define the lag\-type, i.e., how the LAG is

    defined and managed

    .. data:: LACP = 0

    	LAG managed by LACP

    .. data:: STATIC = 1

    	Statically configured bundle / LAG

    """

    LACP = 0

    STATIC = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['AggregationTypeEnum']


class LacpActivityTypeEnum(Enum):
    """
    LacpActivityTypeEnum

    Describes the LACP membership type, active or passive, of the

    interface in the aggregate

    .. data:: ACTIVE = 0

    	Interface is an active member, i.e., will detect and

    	maintain aggregates

    .. data:: PASSIVE = 1

    	Interface is a passive member, i.e., it participates

    	with an active partner

    """

    ACTIVE = 0

    PASSIVE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['LacpActivityTypeEnum']


class LacpPeriodTypeEnum(Enum):
    """
    LacpPeriodTypeEnum

    Defines the period options for the time between sending

    LACP messages

    .. data:: FAST = 0

    	Send LACP packets every second

    .. data:: SLOW = 1

    	Send LACP packets every 30 seconds

    """

    FAST = 0

    SLOW = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['LacpPeriodTypeEnum']


class LacpSynchronizationTypeEnum(Enum):
    """
    LacpSynchronizationTypeEnum

    Indicates LACP synchronization state of participant

    .. data:: IN_SYNC = 0

    	Participant is in sync with the system id and key

    	transmitted

    .. data:: OUT_SYNC = 1

    	Participant is not in sync with the system id and key

    	transmitted

    """

    IN_SYNC = 0

    OUT_SYNC = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['LacpSynchronizationTypeEnum']


class LacpTimeoutTypeEnum(Enum):
    """
    LacpTimeoutTypeEnum

    Type of timeout used, short or long, by LACP participants

    .. data:: LONG = 0

    	Participant wishes to use long timeouts to detect

    	status of the aggregate, i.e., will expect less frequent

    	transmissions. Long timeout is 90 seconds.

    .. data:: SHORT = 1

    	Participant wishes to use short timeouts, i.e., expects

    	frequent transmissions to aggressively detect status

    	changes. Short timeout is 3 seconds.

    """

    LONG = 0

    SHORT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_if_aggregate as meta
        return meta._meta_table['LacpTimeoutTypeEnum']



