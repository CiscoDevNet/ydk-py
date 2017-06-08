


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'TributarySlotGranularityIdentity' : {
        'meta_info' : _MetaInfoClass('TributarySlotGranularityIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'tributary-slot-granularity',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignalIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'TributaryProtocolTypeIdentity' : {
        'meta_info' : _MetaInfoClass('TributaryProtocolTypeIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'tributary-protocol-type',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'Tsg1__Dot__25GIdentity' : {
        'meta_info' : _MetaInfoClass('Tsg1__Dot__25GIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'tsg-1.25G',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'Tsg2__Dot__5GIdentity' : {
        'meta_info' : _MetaInfoClass('Tsg2__Dot__5GIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'tsg-2.5G',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOtu2EIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOtu2EIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-OTU2e',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalFicon4GIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignalFicon4GIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-FICON-4G',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignal10GbeLanIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignal10GbeLanIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-10GbE-LAN',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignal1GbeIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignal1GbeIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-1GbE',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOduflexCbrIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOduflexCbrIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODUFlex-cbr',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignal40GbeIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignal40GbeIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-40GbE',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalFc800Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalFc800Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-FC800',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'Prot40GbeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot40GbeIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-40GbE',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOduflexGfpIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOduflexGfpIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODUFlex-gfp',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignal10GbeWanIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignal10GbeWanIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-10GbE-WAN',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'Prot1GbeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot1GbeIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-1GbE',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalFc400Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalFc400Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-FC400',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOc3_Stm1Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOc3_Stm1Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-OC3_STM1',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOc192_Stm64Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOc192_Stm64Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-OC192_STM64',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOc768_Stm256Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOc768_Stm256Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-OC768_STM256',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOc48_Stm16Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOc48_Stm16Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-OC48_STM16',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOdu3Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu3Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODU3',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOdu2Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu2Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODU2',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOdu1Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu1Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODU1',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOdu0Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu0Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODU0',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOdu4Identity' : {
        'meta_info' : _MetaInfoClass('ProtOdu4Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODU4',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalFicon8GIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignalFicon8GIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-FICON-8G',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignal100GbeIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignal100GbeIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-100GbE',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOducnIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOducnIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODUCn',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOtu3Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu3Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-OTU3',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOtu2Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu2Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-OTU2',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOtu1Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu1Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-OTU1',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOduflexCbrIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOduflexCbrIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODUFlex-cbr',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOdu3Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOdu3Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODU3',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOdu2Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOdu2Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODU2',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOdu1Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOdu1Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODU1',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOtu4Identity' : {
        'meta_info' : _MetaInfoClass('ProtOtu4Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-OTU4',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOdu2EIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOdu2EIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODU2e',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOtucnIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOtucnIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-OTUCn',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOdu0Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOdu0Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODU0',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'Prot10GbeLanIdentity' : {
        'meta_info' : _MetaInfoClass('Prot10GbeLanIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-10GbE-LAN',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOdu2EIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOdu2EIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODU2e',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ProtOduflexGfpIdentity' : {
        'meta_info' : _MetaInfoClass('ProtOduflexGfpIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-ODUFlex-gfp',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOdu4Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOdu4Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODU4',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'Prot100GbeIdentity' : {
        'meta_info' : _MetaInfoClass('Prot100GbeIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'prot-100GbE',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOc12_Stm4Identity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOc12_Stm4Identity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-OC12_STM4',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
    'ClientSignalOducnIdentity' : {
        'meta_info' : _MetaInfoClass('ClientSignalOducnIdentity',
            False, 
            [
            ],
            'ietf-transport-types',
            'client-signal-ODUCn',
            _yang_ns._namespaces['ietf-transport-types'],
        'ydk.models.ietf.ietf_transport_types'
        ),
    },
}
