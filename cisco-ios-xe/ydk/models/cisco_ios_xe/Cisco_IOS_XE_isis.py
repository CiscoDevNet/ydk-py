""" Cisco_IOS_XE_isis 

Cisco XE Native Intermediate System\-to\-Intermediate System (IS\-IS) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AuthenticationLevelTypeEnum(Enum):
    """
    AuthenticationLevelTypeEnum

    .. data:: level_1 = 0

    .. data:: level_2 = 1

    """

    level_1 = 0

    level_2 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_isis as meta
        return meta._meta_table['AuthenticationLevelTypeEnum']


class IsisLevelTypeEnum(Enum):
    """
    IsisLevelTypeEnum

    .. data:: level_1 = 0

    .. data:: level_1_2 = 1

    .. data:: level_2 = 2

    """

    level_1 = 0

    level_1_2 = 1

    level_2 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_isis as meta
        return meta._meta_table['IsisLevelTypeEnum']


class IsisRoutesLevelTypeEnum(Enum):
    """
    IsisRoutesLevelTypeEnum

    .. data:: level_1 = 0

    .. data:: level_1_2 = 1

    .. data:: level_2 = 2

    """

    level_1 = 0

    level_1_2 = 1

    level_2 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_isis as meta
        return meta._meta_table['IsisRoutesLevelTypeEnum']



