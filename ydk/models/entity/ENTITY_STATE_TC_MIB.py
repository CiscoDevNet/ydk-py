""" ENTITY_STATE_TC_MIB 

This MIB defines state textual conventions.

Copyright (C) The Internet Society 2005.  This version
of this MIB module is part of RFC 4268;  see the RFC
itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EntityAdminState_Enum(Enum):
    """
    EntityAdminState_Enum

     Represents the various possible administrative states.
    
    A value of 'locked' means the resource is administratively
    prohibited from use.  A value of 'shuttingDown' means that
    usage is administratively limited to current instances of
    use.  A value of 'unlocked' means the resource is not
    administratively prohibited from use.  A value of
    'unknown' means that this resource is unable to
    report administrative state.

    """

    UNKNOWN = 1

    LOCKED = 2

    SHUTTINGDOWN = 3

    UNLOCKED = 4


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _ENTITY_STATE_TC_MIB as meta
        return meta._meta_table['EntityAdminState_Enum']


class EntityOperState_Enum(Enum):
    """
    EntityOperState_Enum

     Represents the possible values of operational states.
    
    A value of 'disabled' means the resource is totally
    inoperable.  A value of 'enabled' means the resource
    is partially or fully operable.  A value of 'testing'
    means the resource is currently being tested
    and cannot therefore report whether it is operational
    or not.  A value of 'unknown' means that this
    resource is unable to report operational state.

    """

    UNKNOWN = 1

    DISABLED = 2

    ENABLED = 3

    TESTING = 4


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _ENTITY_STATE_TC_MIB as meta
        return meta._meta_table['EntityOperState_Enum']


class EntityStandbyStatus_Enum(Enum):
    """
    EntityStandbyStatus_Enum

     Represents the possible values of standby status.
    
    A value of 'hotStandby' means the resource is not
    providing service, but it will be immediately able to
    take over the role of the resource to be backed up,
    without the need for initialization activity, and will
    contain the same information as the resource to be
    backed up.  A value of 'coldStandy' means that the
    resource is to back up another resource, but will not
    be immediately able to take over the role of a resource
    to be backed up, and will require some initialization
    activity.  A value of 'providingService' means the
    resource is providing service.  A value of
    'unknown' means that this resource is unable to
    report standby state.

    """

    UNKNOWN = 1

    HOTSTANDBY = 2

    COLDSTANDBY = 3

    PROVIDINGSERVICE = 4


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _ENTITY_STATE_TC_MIB as meta
        return meta._meta_table['EntityStandbyStatus_Enum']


class EntityUsageState_Enum(Enum):
    """
    EntityUsageState_Enum

     Represents the possible values of usage states.
    A value of 'idle' means the resource is servicing no
    users.  A value of 'active' means the resource is
    currently in use and it has sufficient spare capacity
    to provide for additional users.  A value of 'busy'
    means the resource is currently in use, but it
    currently has no spare capacity to provide for
    additional users.  A value of 'unknown' means
    that this resource is unable to report usage state.

    """

    UNKNOWN = 1

    IDLE = 2

    ACTIVE = 3

    BUSY = 4


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _ENTITY_STATE_TC_MIB as meta
        return meta._meta_table['EntityUsageState_Enum']


class EntityAlarmStatus_Bits(FixedBitsDict):
    """
    EntityAlarmStatus_Bits

     Represents the possible values of alarm status.
    An Alarm [RFC3877] is a persistent indication
    of an error or warning condition.
    
    When no bits of this attribute are set, then no active
    alarms are known against this entity and it is not under
    repair.
    
    When the 'value of underRepair' is set, the resource is
    currently being repaired, which, depending on the
    implementation, may make the other values in this bit
    string not meaningful.
    
    When the value of 'critical' is set, one or more critical
    alarms are active against the resource.  When the value
    of 'major' is set, one or more major alarms are active
    against the resource.  When the value of 'minor' is set,
    one or more minor alarms are active against the resource.
    When the value of 'warning' is set, one or more warning
    alarms are active against the resource.  When the value
    of 'indeterminate' is set, one or more alarms of whose
    perceived severity cannot be determined are active
    against this resource.
    
    A value of 'unknown' means that this resource is
    unable to report alarm state.
    Keys are:- underRepair , unknown , indeterminate , major , critical , warning , minor

    """

    def __init__(self):
        self._dictionary = { 
            'underRepair':False,
            'unknown':False,
            'indeterminate':False,
            'major':False,
            'critical':False,
            'warning':False,
            'minor':False,
        }
        self._pos_map = { 
            'underRepair':1,
            'unknown':0,
            'indeterminate':6,
            'major':3,
            'critical':2,
            'warning':5,
            'minor':4,
        }


