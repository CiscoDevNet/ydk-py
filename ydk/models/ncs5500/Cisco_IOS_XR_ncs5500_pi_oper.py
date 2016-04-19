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



class CacStateEnum(Enum):
    """
    CacStateEnum

    CAC/UBRL class states

    .. data:: UNKNOWN = 0

    	unknown

    .. data:: ADMIT = 1

    	admit

    .. data:: REDIRECT = 2

    	redirect

    .. data:: UBRL = 3

    	ubrl

    """

    UNKNOWN = 0

    ADMIT = 1

    REDIRECT = 2

    UBRL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_pi_oper as meta
        return meta._meta_table['CacStateEnum']


class PolicyParamUnitEnum(Enum):
    """
    PolicyParamUnitEnum

    Policy param unit

    .. data:: POLICY_PARAM_UNIT_INVALID = 0

    	policy param unit invalid

    .. data:: POLICY_PARAM_UNIT_BYTES = 1

    	policy param unit bytes

    .. data:: POLICY_PARAM_UNIT_KBYTES = 2

    	policy param unit kbytes

    .. data:: POLICY_PARAM_UNIT_MBYTES = 3

    	policy param unit mbytes

    .. data:: POLICY_PARAM_UNIT_GBYTES = 4

    	policy param unit gbytes

    .. data:: POLICY_PARAM_UNIT_BITSPS = 5

    	policy param unit bitsps

    .. data:: POLICY_PARAM_UNIT_KBITSPS = 6

    	policy param unit kbitsps

    .. data:: POLICY_PARAM_UNIT_MBITSPS = 7

    	policy param unit mbitsps

    .. data:: POLICY_PARAM_UNIT_GBITSPS = 8

    	policy param unit gbitsps

    .. data:: POLICY_PARAM_UNIT_CELLS_PS = 9

    	policy param unit cells ps

    .. data:: POLICY_PARAM_UNIT_PACKETS_PS = 10

    	policy param unit packets ps

    .. data:: POLICY_PARAM_UNIT_US = 11

    	policy param unit us

    .. data:: POLICY_PARAM_UNIT_MS = 12

    	policy param unit ms

    .. data:: POLICY_PARAM_UNIT_SECONDS = 13

    	policy param unit seconds

    .. data:: POLICY_PARAM_UNIT_PACKETS = 14

    	policy param unit packets

    .. data:: POLICY_PARAM_UNIT_CELLS = 15

    	policy param unit cells

    .. data:: POLICY_PARAM_UNIT_PERCENT = 16

    	policy param unit percent

    .. data:: POLICY_PARAM_UNIT_PER_THOUSAND = 17

    	policy param unit per thousand

    .. data:: POLICY_PARAM_UNIT_PER_MILLION = 18

    	policy param unit per million

    .. data:: POLICY_PARAM_UNIT_HZ = 19

    	policy param unit hz

    .. data:: POLICY_PARAM_UNIT_KHZ = 20

    	policy param unit khz

    .. data:: POLICY_PARAM_UNIT_MHZ = 21

    	policy param unit mhz

    .. data:: POLICY_PARAM_UNIT_RATIO = 22

    	policy param unit ratio

    .. data:: POLICY_PARAM_UNIT_MAX = 23

    	policy param unit max

    """

    POLICY_PARAM_UNIT_INVALID = 0

    POLICY_PARAM_UNIT_BYTES = 1

    POLICY_PARAM_UNIT_KBYTES = 2

    POLICY_PARAM_UNIT_MBYTES = 3

    POLICY_PARAM_UNIT_GBYTES = 4

    POLICY_PARAM_UNIT_BITSPS = 5

    POLICY_PARAM_UNIT_KBITSPS = 6

    POLICY_PARAM_UNIT_MBITSPS = 7

    POLICY_PARAM_UNIT_GBITSPS = 8

    POLICY_PARAM_UNIT_CELLS_PS = 9

    POLICY_PARAM_UNIT_PACKETS_PS = 10

    POLICY_PARAM_UNIT_US = 11

    POLICY_PARAM_UNIT_MS = 12

    POLICY_PARAM_UNIT_SECONDS = 13

    POLICY_PARAM_UNIT_PACKETS = 14

    POLICY_PARAM_UNIT_CELLS = 15

    POLICY_PARAM_UNIT_PERCENT = 16

    POLICY_PARAM_UNIT_PER_THOUSAND = 17

    POLICY_PARAM_UNIT_PER_MILLION = 18

    POLICY_PARAM_UNIT_HZ = 19

    POLICY_PARAM_UNIT_KHZ = 20

    POLICY_PARAM_UNIT_MHZ = 21

    POLICY_PARAM_UNIT_RATIO = 22

    POLICY_PARAM_UNIT_MAX = 23


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_pi_oper as meta
        return meta._meta_table['PolicyParamUnitEnum']


class PolicyStateEnum(Enum):
    """
    PolicyStateEnum

    Different Interface states

    .. data:: ACTIVE = 0

    	active

    .. data:: SUSPENDED = 1

    	suspended

    """

    ACTIVE = 0

    SUSPENDED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_pi_oper as meta
        return meta._meta_table['PolicyStateEnum']


class WredEnum(Enum):
    """
    WredEnum

    Wred

    .. data:: WRED_COS_CMD = 0

    	wred cos cmd

    .. data:: WRED_DSCP_CMD = 1

    	wred dscp cmd

    .. data:: WRED_PRECEDENCE_CMD = 2

    	wred precedence cmd

    .. data:: WRED_DISCARD_CLASS_CMD = 3

    	wred discard class cmd

    .. data:: WRED_MPLS_EXP_CMD = 4

    	wred mpls exp cmd

    .. data:: RED_WITH_USER_MIN_MAX = 5

    	red with user min max

    .. data:: RED_WITH_DEFAULT_MIN_MAX = 6

    	red with default min max

    .. data:: WRED_DEI_CMD = 7

    	wred dei cmd

    .. data:: WRED_ECN_CMD = 8

    	wred ecn cmd

    .. data:: WRED_INVALID_CMD = 9

    	wred invalid cmd

    """

    WRED_COS_CMD = 0

    WRED_DSCP_CMD = 1

    WRED_PRECEDENCE_CMD = 2

    WRED_DISCARD_CLASS_CMD = 3

    WRED_MPLS_EXP_CMD = 4

    RED_WITH_USER_MIN_MAX = 5

    RED_WITH_DEFAULT_MIN_MAX = 6

    WRED_DEI_CMD = 7

    WRED_ECN_CMD = 8

    WRED_INVALID_CMD = 9


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_pi_oper as meta
        return meta._meta_table['WredEnum']



