


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'MplOps.MplParameter' : {
        'meta_info' : _MetaInfoClass('MplOps.MplParameter',
            False, 
            [
            _MetaInfoClassMember('domainID', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Each domainID must be present in
                mpl-parameter list.
                ''',
                'domainid',
                'ietf-yang-mpl-ops', True),
            _MetaInfoClassMember('CONTROL_MESSAGE_IMAX', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum Trickle timer interval, as defined
                in [RFC6206], for MPL Control Message
                transmissions.
                ''',
                'control_message_imax',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('CONTROL_MESSAGE_IMIN', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The minimum Trickle timer interval, as defined
                in [RFC6206], for MPL Control Message
                transmissions.
                ''',
                'control_message_imin',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('CONTROL_MESSAGE_K', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The redundancy constant, as defined in [RFC6206],
                for MPL Control Message transmissions.
                ''',
                'control_message_k',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('CONTROL_MESSAGE_TIMER_EXPIRATIONS', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The number of Trickle time expirations that occur
                 before terminating the Trickle algorithm
                 for MPL Control Message transmissions.
                ''',
                'control_message_timer_expirations',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('DATA_MESSAGE_IMAX', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum Trickle timer interval, as defined in
                [RFC6206], for MPL Data Message transmissions.
                ''',
                'data_message_imax',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('DATA_MESSAGE_IMIN', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The minimum Trickle timer interval, as defined in
                [RFC6206], for MPL Data Message transmissions.
                ''',
                'data_message_imin',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('DATA_MESSAGE_K', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The redundancy constant, as defined in [RFC6206], for
                MPL Data Message transmissions.
                ''',
                'data_message_k',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('DATA_MESSAGE_TIMER_EXPIRATIONS', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The number of Trickle timer expirations that occur
                before terminating the Trickle algorithm's
                retransmission of a given MPL Data Message.
                ''',
                'data_message_timer_expirations',
                'ietf-yang-mpl-ops', False),
            ],
            'ietf-yang-mpl-ops',
            'mpl-parameter',
            _yang_ns._namespaces['ietf-yang-mpl-ops'],
        'ydk.models.ietf.ietf_yang_mpl_ops'
        ),
    },
    'MplOps' : {
        'meta_info' : _MetaInfoClass('MplOps',
            False, 
            [
            _MetaInfoClassMember('mpl-parameter', REFERENCE_LIST, 'MplParameter' , 'ydk.models.ietf.ietf_yang_mpl_ops', 'MplOps.MplParameter', 
                [], [], 
                '''                Each domain has a set of MPL forwarding parameters
                which regulate the forwarding operation.
                ''',
                'mpl_parameter',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('PROACTIVE_FORWARDING', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The boolean value indicates whether the MPL forwarder
                schedules MPL data message transmission after
                 receiving them for the first time.
                ''',
                'proactive_forwarding',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('SE_LIFETIME', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                lifetime in milliseconds/(mpl timer units),
                 equivalent to SEED_SET_ENTRY_LIFETIME/TUNIT as
                specified in RFC7774.
                ''',
                'se_lifetime',
                'ietf-yang-mpl-ops', False),
            _MetaInfoClassMember('SEED_SET_ENTRY_LIFETIME', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The value indicates the minimum lifetime for an entry
                in the Seed set expressed in seconds. Default value
                is 30 minutes.
                ''',
                'seed_set_entry_lifetime',
                'ietf-yang-mpl-ops', False),
            ],
            'ietf-yang-mpl-ops',
            'mpl-ops',
            _yang_ns._namespaces['ietf-yang-mpl-ops'],
        'ydk.models.ietf.ietf_yang_mpl_ops'
        ),
    },
}
_meta_table['MplOps.MplParameter']['meta_info'].parent =_meta_table['MplOps']['meta_info']
