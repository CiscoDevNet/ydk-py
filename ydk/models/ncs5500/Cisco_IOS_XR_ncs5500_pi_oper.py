""" Cisco_IOS_XR_ncs5500_pi_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-pi package operational data.

This YANG module augments the
  Cisco\-IOS\-XR\-qos\-ma\-oper
module with state data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CacState_Enum(Enum):
    """
    CacState_Enum

    CAC/UBRL class states

    """

    """

    unknown

    """
    UNKNOWN = 0

    """

    admit

    """
    ADMIT = 1

    """

    redirect

    """
    REDIRECT = 2

    """

    ubrl

    """
    UBRL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_pi_oper as meta
        return meta._meta_table['CacState_Enum']


class PolicyParamUnit_Enum(Enum):
    """
    PolicyParamUnit_Enum

    Policy param unit

    """

    """

    policy param unit invalid

    """
    POLICY_PARAM_UNIT_INVALID = 0

    """

    policy param unit bytes

    """
    POLICY_PARAM_UNIT_BYTES = 1

    """

    policy param unit kbytes

    """
    POLICY_PARAM_UNIT_KBYTES = 2

    """

    policy param unit mbytes

    """
    POLICY_PARAM_UNIT_MBYTES = 3

    """

    policy param unit gbytes

    """
    POLICY_PARAM_UNIT_GBYTES = 4

    """

    policy param unit bitsps

    """
    POLICY_PARAM_UNIT_BITSPS = 5

    """

    policy param unit kbitsps

    """
    POLICY_PARAM_UNIT_KBITSPS = 6

    """

    policy param unit mbitsps

    """
    POLICY_PARAM_UNIT_MBITSPS = 7

    """

    policy param unit gbitsps

    """
    POLICY_PARAM_UNIT_GBITSPS = 8

    """

    policy param unit cells ps

    """
    POLICY_PARAM_UNIT_CELLS_PS = 9

    """

    policy param unit packets ps

    """
    POLICY_PARAM_UNIT_PACKETS_PS = 10

    """

    policy param unit us

    """
    POLICY_PARAM_UNIT_US = 11

    """

    policy param unit ms

    """
    POLICY_PARAM_UNIT_MS = 12

    """

    policy param unit seconds

    """
    POLICY_PARAM_UNIT_SECONDS = 13

    """

    policy param unit packets

    """
    POLICY_PARAM_UNIT_PACKETS = 14

    """

    policy param unit cells

    """
    POLICY_PARAM_UNIT_CELLS = 15

    """

    policy param unit percent

    """
    POLICY_PARAM_UNIT_PERCENT = 16

    """

    policy param unit per thousand

    """
    POLICY_PARAM_UNIT_PER_THOUSAND = 17

    """

    policy param unit per million

    """
    POLICY_PARAM_UNIT_PER_MILLION = 18

    """

    policy param unit hz

    """
    POLICY_PARAM_UNIT_HZ = 19

    """

    policy param unit khz

    """
    POLICY_PARAM_UNIT_KHZ = 20

    """

    policy param unit mhz

    """
    POLICY_PARAM_UNIT_MHZ = 21

    """

    policy param unit ratio

    """
    POLICY_PARAM_UNIT_RATIO = 22

    """

    policy param unit max

    """
    POLICY_PARAM_UNIT_MAX = 23


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_pi_oper as meta
        return meta._meta_table['PolicyParamUnit_Enum']


class PolicyState_Enum(Enum):
    """
    PolicyState_Enum

    Different Interface states

    """

    """

    active

    """
    ACTIVE = 0

    """

    suspended

    """
    SUSPENDED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_pi_oper as meta
        return meta._meta_table['PolicyState_Enum']


class Wred_Enum(Enum):
    """
    Wred_Enum

    Wred

    """

    """

    wred cos cmd

    """
    WRED_COS_CMD = 0

    """

    wred dscp cmd

    """
    WRED_DSCP_CMD = 1

    """

    wred precedence cmd

    """
    WRED_PRECEDENCE_CMD = 2

    """

    wred discard class cmd

    """
    WRED_DISCARD_CLASS_CMD = 3

    """

    wred mpls exp cmd

    """
    WRED_MPLS_EXP_CMD = 4

    """

    red with user min max

    """
    RED_WITH_USER_MIN_MAX = 5

    """

    red with default min max

    """
    RED_WITH_DEFAULT_MIN_MAX = 6

    """

    wred dei cmd

    """
    WRED_DEI_CMD = 7

    """

    wred ecn cmd

    """
    WRED_ECN_CMD = 8

    """

    wred invalid cmd

    """
    WRED_INVALID_CMD = 9


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_pi_oper as meta
        return meta._meta_table['Wred_Enum']



