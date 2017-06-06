""" Cisco_IOS_XE_policy 

Cisco XE Native Policy Map Yang Model.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ClassNameTypeEnum(Enum):
    """
    ClassNameTypeEnum

    .. data:: class_default = 0

    """

    class_default = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_policy as meta
        return meta._meta_table['ClassNameTypeEnum']


class PolicePacketsBytesTypeEnum(Enum):
    """
    PolicePacketsBytesTypeEnum

    .. data:: packets = 0

    .. data:: bytes = 1

    """

    packets = 0

    bytes = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_policy as meta
        return meta._meta_table['PolicePacketsBytesTypeEnum']


class PolicePpsBpsTypeEnum(Enum):
    """
    PolicePpsBpsTypeEnum

    .. data:: pps = 0

    .. data:: bps = 1

    """

    pps = 0

    bps = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_policy as meta
        return meta._meta_table['PolicePpsBpsTypeEnum']


class PolicyActionTypeEnum(Enum):
    """
    PolicyActionTypeEnum

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

    bandwidth = 0

    compression = 1

    drop = 2

    estimate = 3

    fair_queue = 4

    forward = 5

    netflow_sampler = 6

    police = 7

    priority = 8

    queue_limit = 9

    random_detect = 10

    service_policy = 11

    set = 12

    shape = 13

    trust = 14

    dbl = 15

    queue_buffers = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_policy as meta
        return meta._meta_table['PolicyActionTypeEnum']


class PrecedenceType2Enum(Enum):
    """
    PrecedenceType2Enum

    .. data:: rsvp = 0

    """

    rsvp = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_policy as meta
        return meta._meta_table['PrecedenceType2Enum']



