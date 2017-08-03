""" ENTITY_STATE_TC_MIB 

This MIB defines state textual conventions.

Copyright (C) The Internet Society 2005.  This version
of this MIB module is part of RFC 4268;  see the RFC
itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Entityadminstate(Enum):
    """
    Entityadminstate

     Represents the various possible administrative states.

    A value of 'locked' means the resource is administratively

    prohibited from use.  A value of 'shuttingDown' means that

    usage is administratively limited to current instances of

    use.  A value of 'unlocked' means the resource is not

    administratively prohibited from use.  A value of

    'unknown' means that this resource is unable to

    report administrative state.

    .. data:: unknown = 1

    .. data:: locked = 2

    .. data:: shuttingDown = 3

    .. data:: unlocked = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    locked = Enum.YLeaf(2, "locked")

    shuttingDown = Enum.YLeaf(3, "shuttingDown")

    unlocked = Enum.YLeaf(4, "unlocked")


class Entityoperstate(Enum):
    """
    Entityoperstate

     Represents the possible values of operational states.

    A value of 'disabled' means the resource is totally

    inoperable.  A value of 'enabled' means the resource

    is partially or fully operable.  A value of 'testing'

    means the resource is currently being tested

    and cannot therefore report whether it is operational

    or not.  A value of 'unknown' means that this

    resource is unable to report operational state.

    .. data:: unknown = 1

    .. data:: disabled = 2

    .. data:: enabled = 3

    .. data:: testing = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    disabled = Enum.YLeaf(2, "disabled")

    enabled = Enum.YLeaf(3, "enabled")

    testing = Enum.YLeaf(4, "testing")


class Entitystandbystatus(Enum):
    """
    Entitystandbystatus

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

    .. data:: unknown = 1

    .. data:: hotStandby = 2

    .. data:: coldStandby = 3

    .. data:: providingService = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    hotStandby = Enum.YLeaf(2, "hotStandby")

    coldStandby = Enum.YLeaf(3, "coldStandby")

    providingService = Enum.YLeaf(4, "providingService")


class Entityusagestate(Enum):
    """
    Entityusagestate

     Represents the possible values of usage states.

    A value of 'idle' means the resource is servicing no

    users.  A value of 'active' means the resource is

    currently in use and it has sufficient spare capacity

    to provide for additional users.  A value of 'busy'

    means the resource is currently in use, but it

    currently has no spare capacity to provide for

    additional users.  A value of 'unknown' means

    that this resource is unable to report usage state.

    .. data:: unknown = 1

    .. data:: idle = 2

    .. data:: active = 3

    .. data:: busy = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    idle = Enum.YLeaf(2, "idle")

    active = Enum.YLeaf(3, "active")

    busy = Enum.YLeaf(4, "busy")


class Entityalarmstatus(Bits):
    """
    Entityalarmstatus

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
    Keys are:- critical , underRepair , minor , indeterminate , major , unknown , warning

    """

    def __init__(self):
        super(Entityalarmstatus, self).__init__()


