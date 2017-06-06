""" Cisco_IOS_XE_utd 

Cisco XE Native Unified Threat Defense (UTD) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SyslogLevelTypeEnum(Enum):
    """
    SyslogLevelTypeEnum

    .. data:: alert = 0

    .. data:: crit = 1

    .. data:: debug = 2

    .. data:: emerg = 3

    .. data:: err = 4

    .. data:: info = 5

    .. data:: notice = 6

    .. data:: warning = 7

    """

    alert = 0

    crit = 1

    debug = 2

    emerg = 3

    err = 4

    info = 5

    notice = 6

    warning = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_utd as meta
        return meta._meta_table['SyslogLevelTypeEnum']



