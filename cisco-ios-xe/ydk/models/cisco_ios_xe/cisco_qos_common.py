""" cisco_qos_common 

This module contains YANG definitions for
common units for qos

Copyright (c) 2015 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ThreshUnit(Enum):
    """
    ThreshUnit

    Unit for threshold

    .. data:: default = 0

    .. data:: bytes = 1

    .. data:: sec = 2

    .. data:: packets = 3

    .. data:: cells = 4

    .. data:: percent = 5

    """

    default = Enum.YLeaf(0, "default")

    bytes = Enum.YLeaf(1, "bytes")

    sec = Enum.YLeaf(2, "sec")

    packets = Enum.YLeaf(3, "packets")

    cells = Enum.YLeaf(4, "cells")

    percent = Enum.YLeaf(5, "percent")



