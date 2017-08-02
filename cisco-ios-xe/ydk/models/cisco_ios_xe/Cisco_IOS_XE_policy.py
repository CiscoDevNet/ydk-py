""" Cisco_IOS_XE_policy 

Cisco XE Native Policy Map Yang Model.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ClassNameType(Enum):
    """
    ClassNameType

    .. data:: class_default = 0

    """

    class_default = Enum.YLeaf(0, "class-default")


class PolicePacketsBytesType(Enum):
    """
    PolicePacketsBytesType

    .. data:: packets = 0

    .. data:: bytes = 1

    """

    packets = Enum.YLeaf(0, "packets")

    bytes = Enum.YLeaf(1, "bytes")


class PolicePpsBpsType(Enum):
    """
    PolicePpsBpsType

    .. data:: pps = 0

    .. data:: bps = 1

    """

    pps = Enum.YLeaf(0, "pps")

    bps = Enum.YLeaf(1, "bps")


class PolicyActionType(Enum):
    """
    PolicyActionType

    .. data:: bandwidth = 0

    .. data:: compression = 1

    .. data:: drop = 2

    .. data:: estimate = 3

    .. data:: fair_queue = 4

    .. data:: forward = 5

    .. data:: netflow_sampler = 6

    .. data:: police = 7

    .. data:: priority = 8

    .. data:: queue_limit = 9

    .. data:: random_detect = 10

    .. data:: service_policy = 11

    .. data:: set = 12

    .. data:: shape = 13

    .. data:: trust = 14

    .. data:: dbl = 15

    .. data:: queue_buffers = 16

    """

    bandwidth = Enum.YLeaf(0, "bandwidth")

    compression = Enum.YLeaf(1, "compression")

    drop = Enum.YLeaf(2, "drop")

    estimate = Enum.YLeaf(3, "estimate")

    fair_queue = Enum.YLeaf(4, "fair-queue")

    forward = Enum.YLeaf(5, "forward")

    netflow_sampler = Enum.YLeaf(6, "netflow-sampler")

    police = Enum.YLeaf(7, "police")

    priority = Enum.YLeaf(8, "priority")

    queue_limit = Enum.YLeaf(9, "queue-limit")

    random_detect = Enum.YLeaf(10, "random-detect")

    service_policy = Enum.YLeaf(11, "service-policy")

    set = Enum.YLeaf(12, "set")

    shape = Enum.YLeaf(13, "shape")

    trust = Enum.YLeaf(14, "trust")

    dbl = Enum.YLeaf(15, "dbl")

    queue_buffers = Enum.YLeaf(16, "queue-buffers")


class PrecedenceType2(Enum):
    """
    PrecedenceType2

    .. data:: rsvp = 0

    """

    rsvp = Enum.YLeaf(0, "rsvp")



