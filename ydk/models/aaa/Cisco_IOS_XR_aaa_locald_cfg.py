""" Cisco_IOS_XR_aaa_locald_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-lib\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AaaLocaldTaskClass_Enum(Enum):
    """
    AaaLocaldTaskClass_Enum

    Aaa locald task class

    """

    """

    Permits read operation for a Task ID

    """
    READ = 0

    """

    Permits write operation for a Task ID

    """
    WRITE = 1

    """

    Permits execute operation for a Task ID

    """
    EXECUTE = 2

    """

    Permits debug operation for a Task ID

    """
    DEBUG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_cfg as meta
        return meta._meta_table['AaaLocaldTaskClass_Enum']



