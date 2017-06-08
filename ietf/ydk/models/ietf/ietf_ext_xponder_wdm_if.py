""" ietf_ext_xponder_wdm_if 

This module contains a collection of YANG definitions for
configuring Optical interfaces.

Copyright (c) 2016 IETF Trust and the persons identified
as authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and
subject to the license terms contained in, the Simplified
BSD License set forth in Section 4.c of the IETF Trust's
Legal Provisions Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class OptIfOchTcaTypesEnum(Enum):
    """
    OptIfOchTcaTypesEnum

     The different types of TCA's

    .. data:: min_tx_power_tca = 0

    	 The min tx power tca

    .. data:: max_tx_power_tca = 1

    	 The min tx power tca

    .. data:: min_rx_power_tca = 2

    	 The min tx power tca

    .. data:: max_rx_power_tca = 3

    	 The min tx power tca

    .. data:: min_frequency_offset_tca = 4

    	 Min Frequency offset tca

    .. data:: max_frequency_offset_tca = 5

    	 Max Frequency offset tca

    .. data:: min_osnr_tca = 6

    	 Min OSNR tca

    .. data:: max_osnr_tca = 7

    	 Max OSNR tca

    .. data:: min_laser_temperature_tca = 8

    	 The min tx power tca

    .. data:: max_laser_temperature_tca = 9

    	 Temperature tca

    .. data:: min_fec_ber_tca = 10

    	 Min Pre Fec BER tca

    .. data:: max_fec_ber_tca = 11

    	 Max Pre Fec BER tca

    .. data:: min_q_tca = 12

    	Min Q tca

    .. data:: max_q_tca = 13

    	Max Q tca

    """

    min_tx_power_tca = 0

    max_tx_power_tca = 1

    min_rx_power_tca = 2

    max_rx_power_tca = 3

    min_frequency_offset_tca = 4

    max_frequency_offset_tca = 5

    min_osnr_tca = 6

    max_osnr_tca = 7

    min_laser_temperature_tca = 8

    max_laser_temperature_tca = 9

    min_fec_ber_tca = 10

    max_fec_ber_tca = 11

    min_q_tca = 12

    max_q_tca = 13


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_ext_xponder_wdm_if as meta
        return meta._meta_table['OptIfOchTcaTypesEnum']



