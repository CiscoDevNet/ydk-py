


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'OptIfOchTcaTypesEnum' : _MetaInfoEnum('OptIfOchTcaTypesEnum', 'ydk.models.ietf.ietf_ext_xponder_wdm_if',
        {
            'min-tx-power-tca':'min_tx_power_tca',
            'max-tx-power-tca':'max_tx_power_tca',
            'min-rx-power-tca':'min_rx_power_tca',
            'max-rx-power-tca':'max_rx_power_tca',
            'min-frequency-offset-tca':'min_frequency_offset_tca',
            'max-frequency-offset-tca':'max_frequency_offset_tca',
            'min-osnr-tca':'min_osnr_tca',
            'max-osnr-tca':'max_osnr_tca',
            'min-laser-temperature-tca':'min_laser_temperature_tca',
            'max-laser-temperature-tca':'max_laser_temperature_tca',
            'min-fec-ber-tca':'min_fec_ber_tca',
            'max-fec-ber-tca':'max_fec_ber_tca',
            'min-q-tca':'min_q_tca',
            'max-q-tca':'max_q_tca',
        }, 'ietf-ext-xponder-wdm-if', _yang_ns._namespaces['ietf-ext-xponder-wdm-if']),
}
