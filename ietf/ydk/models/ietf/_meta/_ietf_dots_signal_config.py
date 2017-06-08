


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'SignalConfig' : {
        'meta_info' : _MetaInfoClass('SignalConfig',
            False, 
            [
            _MetaInfoClassMember('ack-random-factor', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Random factor used to influence the timing of
                retransmissions
                ''',
                'ack_random_factor',
                'ietf-dots-signal-config', False),
            _MetaInfoClassMember('ack-timeout', ATTRIBUTE, 'int' , None, None, 
                [('-32768', '32767')], [], 
                '''                Initial retransmission timeout value
                ''',
                'ack_timeout',
                'ietf-dots-signal-config', False),
            _MetaInfoClassMember('heartbeat-interval', ATTRIBUTE, 'int' , None, None, 
                [('-32768', '32767')], [], 
                '''                heartbeat interval
                ''',
                'heartbeat_interval',
                'ietf-dots-signal-config', False),
            _MetaInfoClassMember('max-retransmit', ATTRIBUTE, 'int' , None, None, 
                [('-32768', '32767')], [], 
                '''                Maximum number of retransmissions
                ''',
                'max_retransmit',
                'ietf-dots-signal-config', False),
            _MetaInfoClassMember('policy-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Identifier for the DOTS signal channel
                session configuration data
                ''',
                'policy_id',
                'ietf-dots-signal-config', False),
            ],
            'ietf-dots-signal-config',
            'signal-config',
            _yang_ns._namespaces['ietf-dots-signal-config'],
        'ydk.models.ietf.ietf_dots_signal_config'
        ),
    },
}
