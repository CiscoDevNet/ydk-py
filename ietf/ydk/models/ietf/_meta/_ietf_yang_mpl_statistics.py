


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'MplStatistics' : {
        'meta_info' : _MetaInfoClass('MplStatistics',
            False, 
            [
            _MetaInfoClassMember('domainID', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                together with seed-ID uniquely identifies buffer set.
                ''',
                'domainid',
                'ietf-yang-mpl-statistics', True),
            _MetaInfoClassMember('seedID', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                value uniquely identifies the MPL Seed within a MPL
                domain.
                ''',
                'seedid',
                'ietf-yang-mpl-statistics', True),
            _MetaInfoClassMember('c-too-high', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of times that a copy was not forwarded
                  because c > k.
                ''',
                'c_too_high',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-forwarded', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of times copies are forwarded, while c <= k.
                ''',
                'nr_forwarded',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-consistent-control', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of consistent control messages.
                ''',
                'nr_of_consistent_control',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-consistent-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of consistent data messages.
                ''',
                'nr_of_consistent_data',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-copies-forwarded', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of forwarded copies, can be larger than
                number-of-copies-received.
                ''',
                'nr_of_copies_forwarded',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-copies-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                total number of message copies received.
                ''',
                'nr_of_copies_received',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-inconsistent-control', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of inconsistent control messages.
                ''',
                'nr_of_inconsistent_control',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-inconsistent-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of inconsistent data messages.
                ''',
                'nr_of_inconsistent_data',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-messages-forwarded', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of forwarded messages, must be smaller than or
                equal to nr-of-messages-received.
                ''',
                'nr_of_messages_forwarded',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-messages-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of messages (one or more copies) received,
                must be smaller than or equal to seqno.
                ''',
                'nr_of_messages_received',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-missed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of messages that were not received
                (derived from gaps in received seqno's.)
                ''',
                'nr_of_missed',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-notreceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of messages that were not received
                according to control message.
                ''',
                'nr_of_notreceived',
                'ietf-yang-mpl-statistics', False),
            _MetaInfoClassMember('nr-of-refused', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of refused copies because seqno too small.
                ''',
                'nr_of_refused',
                'ietf-yang-mpl-statistics', False),
            ],
            'ietf-yang-mpl-statistics',
            'mpl-statistics',
            _yang_ns._namespaces['ietf-yang-mpl-statistics'],
        'ydk.models.ietf.ietf_yang_mpl_statistics'
        ),
    },
}
