
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Components.Component.OpticalChannel.State.InputPower.avg' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.InputPower.instant' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.InputPower.max' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.InputPower.min' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.LaserBiasCurrent.avg' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.LaserBiasCurrent.instant' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.LaserBiasCurrent.max' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.LaserBiasCurrent.min' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.OutputPower.avg' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.OutputPower.instant' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.OutputPower.max' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.OutputPower.min' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.PolarizationModeDispersion.avg' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.PolarizationModeDispersion.instant' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.PolarizationModeDispersion.max' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.PolarizationModeDispersion.min' : {
        'deviation_typ' : 'not_supported',
    },
    'Components.Component.OpticalChannel.State.group_id' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Ethernet.State.in_8021q_frames' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Ethernet.State.in_mac_control_frames' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Ethernet.State.out_8021q_frames' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Ethernet.State.out_mac_control_frames' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.Config.tti_msg_auto' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr.avg' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr.instant' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr.max' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.Esnr.min' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.QValue.avg' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.QValue.instant' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.QValue.max' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.QValue.min' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.code_violations' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.fec_corrected_bytes' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.rdi_msg' : {
        'deviation_typ' : 'not_supported',
    },
    'TerminalDevice.LogicalChannels.Channel.Otn.State.tti_msg_auto' : {
        'deviation_typ' : 'not_supported',
    },
}
