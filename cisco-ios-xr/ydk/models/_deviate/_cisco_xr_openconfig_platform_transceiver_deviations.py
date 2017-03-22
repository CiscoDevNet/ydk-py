
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Components.Component.Transceiver.Config.enabled' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.Transceiver.Config.form_factor' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.Config.target_output_power' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.Config.tx_laser' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.State.target_output_power' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.Transceiver.PhysicalChannels.Channel.State.tx_laser' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.Transceiver.State.enabled' : {
        'deviation_typ' : 'not_supported',
    },
}
