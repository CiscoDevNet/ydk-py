


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IfdirectionEnum' : _MetaInfoEnum('IfdirectionEnum', 'ydk.models.cisco_ios_xe.DIFFSERV_MIB',
        {
            'inbound':'inbound',
            'outbound':'outbound',
        }, 'DIFFSERV-MIB', _yang_ns._namespaces['DIFFSERV-MIB']),
    'DiffservtbparamtrtcmawareIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservtbparamtrtcmawareIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServTBParamTrTCMAware',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservtbparamsrtcmawareIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservtbparamsrtcmawareIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServTBParamSrTCMAware',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservtbparamavgrateIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservtbparamavgrateIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServTBParamAvgRate',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservtbparamsrtcmblindIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservtbparamsrtcmblindIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServTBParamSrTCMBlind',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservtbparamtrtcmblindIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservtbparamtrtcmblindIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServTBParamTrTCMBlind',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservschedulerwfqIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservschedulerwfqIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServSchedulerWFQ',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservtbparamtswtcmIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservtbparamtswtcmIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServTBParamTswTCM',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservtbparamsimpletokenbucketIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservtbparamsimpletokenbucketIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServTBParamSimpleTokenBucket',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservschedulerwrrIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservschedulerwrrIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServSchedulerWRR',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservschedulerpriorityIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservschedulerpriorityIdentity',
            False, 
            [
            ],
            'DIFFSERV-MIB',
            'diffServSchedulerPriority',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservclassifier' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservclassifier',
            False, 
            [
            _MetaInfoClassMember('diffServClfrElementNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServClfrElementId,
                or a zero to indicate that none exist.
                ''',
                'diffservclfrelementnextfree',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClfrNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServClfrId, or a
                zero to indicate that none exist.
                ''',
                'diffservclfrnextfree',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for
                diffServMultiFieldClfrId, or a zero to indicate that none exist.
                ''',
                'diffservmultifieldclfrnextfree',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServClassifier',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservmeter' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservmeter',
            False, 
            [
            _MetaInfoClassMember('diffServMeterNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServMeterId, or a
                zero to indicate that none exist.
                ''',
                'diffservmeternextfree',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMeter',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservtbparam' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservtbparam',
            False, 
            [
            _MetaInfoClassMember('diffServTBParamNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServTBParamId, or a
                zero to indicate that none exist.
                ''',
                'diffservtbparamnextfree',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServTBParam',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservaction' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservaction',
            False, 
            [
            _MetaInfoClassMember('diffServActionNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServActionId, or a
                zero to indicate that none exist.
                ''',
                'diffservactionnextfree',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServCountActNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for
                diffServCountActId, or a zero to indicate that none exist.
                ''',
                'diffservcountactnextfree',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServAction',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservalgdrop' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservalgdrop',
            False, 
            [
            _MetaInfoClassMember('diffServAlgDropNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServAlgDropId, or a
                zero to indicate that none exist.
                ''',
                'diffservalgdropnextfree',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServRandomDropId,
                or a zero to indicate that none exist.
                ''',
                'diffservrandomdropnextfree',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServAlgDrop',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservqueue' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservqueue',
            False, 
            [
            _MetaInfoClassMember('diffServQNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServQId, or a zero
                to indicate that none exist.
                ''',
                'diffservqnextfree',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServQueue',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservscheduler' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservscheduler',
            False, 
            [
            _MetaInfoClassMember('diffServMaxRateNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServMaxRateId, or a
                zero to indicate that none exist.
                ''',
                'diffservmaxratenextfree',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMinRateNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServMinRateId, or a
                zero to indicate that none exist.
                ''',
                'diffservminratenextfree',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServSchedulerNextFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an unused value for diffServSchedulerId, or
                a zero to indicate that none exist.
                ''',
                'diffservschedulernextfree',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServScheduler',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservdatapathtable.Diffservdatapathentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservdatapathtable.Diffservdatapathentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServDataPathIfDirection', REFERENCE_ENUM_CLASS, 'IfdirectionEnum' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'IfdirectionEnum', 
                [], [], 
                '''                IfDirection specifies whether the reception or transmission path
                for this interface is in view.
                ''',
                'diffservdatapathifdirection',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServDataPathStart', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This selects the first Differentiated Services Functional Data
                Path Element to handle traffic for this data path. This
                RowPointer should point to an instance of one of:
                  diffServClfrEntry
                  diffServMeterEntry
                  diffServActionEntry
                  diffServAlgDropEntry
                  diffServQEntry
                
                A value of zeroDotZero in this attribute indicates that no
                Differentiated Services treatment is performed on traffic of this
                data path. A pointer with the value zeroDotZero normally
                terminates a functional data path.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservdatapathstart',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServDataPathStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time.
                ''',
                'diffservdatapathstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServDataPathStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservdatapathstorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServDataPathEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservdatapathtable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservdatapathtable',
            False, 
            [
            _MetaInfoClassMember('diffServDataPathEntry', REFERENCE_LIST, 'Diffservdatapathentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservdatapathtable.Diffservdatapathentry', 
                [], [], 
                '''                An entry in the data path table indicates the start of a single
                Differentiated Services Functional Data Path in this device.
                
                These are associated with individual interfaces, logical or
                physical, and therefore are instantiated by ifIndex. Therefore,
                the interface index must have been assigned, according to the
                procedures applicable to that, before it can be meaningfully
                used. Generally, this means that the interface must exist.
                
                When diffServDataPathStorage is of type nonVolatile, however,
                this may reflect the configuration for an interface whose ifIndex
                has been assigned but for which the supporting implementation is
                not currently present.
                ''',
                'diffservdatapathentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServDataPathTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservclfrtable.Diffservclfrentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservclfrtable.Diffservclfrentry',
            False, 
            [
            _MetaInfoClassMember('diffServClfrId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the classifier entries.  Managers
                should obtain new values for row creation in this table by
                reading diffServClfrNextFree.
                ''',
                'diffservclfrid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServClfrStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservclfrstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClfrStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservclfrstorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServClfrEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservclfrtable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservclfrtable',
            False, 
            [
            _MetaInfoClassMember('diffServClfrEntry', REFERENCE_LIST, 'Diffservclfrentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservclfrtable.Diffservclfrentry', 
                [], [], 
                '''                An entry in the classifier table describes a single classifier.
                All classifier elements belonging to the same classifier use the
                classifier's diffServClfrId as part of their index.
                ''',
                'diffservclfrentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServClfrTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry',
            False, 
            [
            _MetaInfoClassMember('diffServClfrId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'diffservclfrid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServClfrElementId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Classifier Element entries.
                Managers obtain new values for row creation in this table by
                reading diffServClfrElementNextFree.
                ''',
                'diffservclfrelementid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServClfrElementNext', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This attribute provides one branch of the fan-out functionality
                of a classifier described in the Informal Differentiated Services
                Model section 4.1.
                
                This selects the next Differentiated Services Functional Data
                Path Element to handle traffic for this data path. This
                RowPointer should point to an instance of one of:
                  diffServClfrEntry
                  diffServMeterEntry
                  diffServActionEntry
                  diffServAlgDropEntry
                  diffServQEntry
                
                A value of zeroDotZero in this attribute indicates no further
                Differentiated Services treatment is performed on traffic of this
                data path. The use of zeroDotZero is the normal usage for the
                last functional data path element of the current data path.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservclfrelementnext',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClfrElementPrecedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The relative order in which classifier elements are applied:
                higher numbers represent classifier element with higher
                precedence.  Classifier elements with the same order must be
                unambiguous i.e. they must define non-overlapping patterns, and
                are considered to be applied simultaneously to the traffic
                stream. Classifier elements with different order may overlap in
                their filters:  the classifier element with the highest order
                that matches is taken.
                
                On a given interface, there must be a complete classifier in
                place at all times in the ingress direction.  This means one or
                more filters must match any possible pattern. There is no such
                
                
                
                requirement in the egress direction.
                ''',
                'diffservclfrelementprecedence',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClfrElementSpecific', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A pointer to a valid entry in another table, filter table, that
                describes the applicable classification parameters, e.g. an entry
                in diffServMultiFieldClfrTable.
                
                The value zeroDotZero is interpreted to match anything not
                matched by another classifier element - only one such entry may
                exist for each classifier.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                
                
                
                becomes inactive by other means, the element is ignored.
                ''',
                'diffservclfrelementspecific',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClfrElementStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservclfrelementstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClfrElementStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservclfrelementstorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServClfrElementEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservclfrelementtable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservclfrelementtable',
            False, 
            [
            _MetaInfoClassMember('diffServClfrElementEntry', REFERENCE_LIST, 'Diffservclfrelemententry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry', 
                [], [], 
                '''                An entry in the classifier element table describes a single
                element of the classifier.
                ''',
                'diffservclfrelemententry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServClfrElementTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry',
            False, 
            [
            _MetaInfoClassMember('diffServMultiFieldClfrId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the MultiField Classifier filter
                entries.  Managers obtain new values for row creation in this
                table by reading diffServMultiFieldClfrNextFree.
                ''',
                'diffservmultifieldclfrid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServMultiFieldClfrAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of IP address used by this classifier entry.  While
                other types of addresses are defined in the InetAddressType
                
                
                
                textual convention, and DNS names, a classifier can only look at
                packets on the wire. Therefore, this object is limited to IPv4
                and IPv6 addresses.
                ''',
                'diffservmultifieldclfraddrtype',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrDscp', ATTRIBUTE, 'int' , None, None, 
                [('-1', '63')], [], 
                '''                The value that the DSCP in the packet must have to match this
                entry. A value of -1 indicates that a specific DSCP value has not
                been defined and thus all DSCP values are considered a match.
                ''',
                'diffservmultifieldclfrdscp',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrDstAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address to match against the packet's destination IP
                address. This may not be a DNS name, but may be an IPv4 or IPv6
                prefix.  diffServMultiFieldClfrDstPrefixLength indicates the
                number of bits that are relevant.
                ''',
                'diffservmultifieldclfrdstaddr',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrDstL4PortMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum value that the layer-4 destination port number in
                the packet must have in order to match this classifier entry.
                This value must be equal to or greater than the value specified
                for this entry in diffServMultiFieldClfrDstL4PortMin.
                ''',
                'diffservmultifieldclfrdstl4portmax',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrDstL4PortMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The minimum value that the layer-4 destination port number in
                the packet must have in order to match this classifier entry.
                ''',
                'diffservmultifieldclfrdstl4portmin',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrDstPrefixLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                The length of the CIDR Prefix carried in
                diffServMultiFieldClfrDstAddr. In IPv4 addresses, a length of 0
                indicates a match of any address; a length of 32 indicates a
                match of a single host address, and a length between 0 and 32
                indicates the use of a CIDR Prefix. IPv6 is similar, except that
                prefix lengths range from 0..128.
                ''',
                'diffservmultifieldclfrdstprefixlength',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrFlowId', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                The flow identifier in an IPv6 header.
                ''',
                'diffservmultifieldclfrflowid',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrProtocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The IP protocol to match against the IPv4 protocol number or the
                IPv6 Next- Header number in the packet. A value of 255 means
                match all.  Note the protocol number of 255 is reserved by IANA,
                and Next-Header number of 0 is used in IPv6.
                ''',
                'diffservmultifieldclfrprotocol',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrSrcAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address to match against the packet's source IP address.
                This may not be a DNS name, but may be an IPv4 or IPv6 prefix.
                diffServMultiFieldClfrSrcPrefixLength indicates the number of
                bits that are relevant.
                ''',
                'diffservmultifieldclfrsrcaddr',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrSrcL4PortMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum value that the layer-4 source port number in the
                packet must have in order to match this classifier entry. This
                value must be equal to or greater than the value specified for
                this entry in diffServMultiFieldClfrSrcL4PortMin.
                ''',
                'diffservmultifieldclfrsrcl4portmax',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrSrcL4PortMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The minimum value that the layer-4 source port number in the
                packet must have in order to match this classifier entry.
                ''',
                'diffservmultifieldclfrsrcl4portmin',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrSrcPrefixLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                The length of the CIDR Prefix carried in
                diffServMultiFieldClfrSrcAddr. In IPv4 addresses, a length of 0
                indicates a match of any address; a length of 32 indicates a
                match of a single host address, and a length between 0 and 32
                indicates the use of a CIDR Prefix. IPv6 is similar, except that
                prefix lengths range from 0..128.
                ''',
                'diffservmultifieldclfrsrcprefixlength',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservmultifieldclfrstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservmultifieldclfrstorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMultiFieldClfrEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservmultifieldclfrtable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservmultifieldclfrtable',
            False, 
            [
            _MetaInfoClassMember('diffServMultiFieldClfrEntry', REFERENCE_LIST, 'Diffservmultifieldclfrentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry', 
                [], [], 
                '''                An IP Multi-field Classifier entry describes a single filter.
                ''',
                'diffservmultifieldclfrentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMultiFieldClfrTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservmetertable.Diffservmeterentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservmetertable.Diffservmeterentry',
            False, 
            [
            _MetaInfoClassMember('diffServMeterId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Meter entries.  Managers obtain new
                values for row creation in this table by reading
                diffServMeterNextFree.
                ''',
                'diffservmeterid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServMeterFailNext', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                If the traffic does not conform, this selects the next
                Differentiated Services Functional Data Path element to handle
                traffic for this data path. This RowPointer should point to an
                instance of one of:
                  diffServClfrEntry
                  diffServMeterEntry
                
                
                
                  diffServActionEntry
                  diffServAlgDropEntry
                  diffServQEntry
                
                A value of zeroDotZero in this attribute indicates no further
                Differentiated Services treatment is performed on traffic of this
                data path. The use of zeroDotZero is the normal usage for the
                last functional data path element of the current data path.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservmeterfailnext',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMeterSpecific', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This indicates the behavior of the meter by pointing to an entry
                containing detailed parameters. Note that entries in that
                specific table must be managed explicitly.
                
                For example, diffServMeterSpecific may point to an entry in
                diffServTBParamTable, which contains an instance of a single set
                of Token Bucket parameters.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the meter always succeeds.
                ''',
                'diffservmeterspecific',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMeterStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservmeterstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMeterStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservmeterstorage',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMeterSucceedNext', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                If the traffic does conform, this selects the next
                Differentiated Services Functional Data Path element to handle
                traffic for this data path. This RowPointer should point to an
                instance of one of:
                  diffServClfrEntry
                  diffServMeterEntry
                  diffServActionEntry
                  diffServAlgDropEntry
                  diffServQEntry
                
                A value of zeroDotZero in this attribute indicates that no
                further Differentiated Services treatment is performed on traffic
                of this data path. The use of zeroDotZero is the normal usage for
                the last functional data path element of the current data path.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservmetersucceednext',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMeterEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservmetertable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservmetertable',
            False, 
            [
            _MetaInfoClassMember('diffServMeterEntry', REFERENCE_LIST, 'Diffservmeterentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservmetertable.Diffservmeterentry', 
                [], [], 
                '''                An entry in the meter table describes a single conformance level
                of a meter.
                ''',
                'diffservmeterentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMeterTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservtbparamtable.Diffservtbparamentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservtbparamtable.Diffservtbparamentry',
            False, 
            [
            _MetaInfoClassMember('diffServTBParamId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Token Bucket Parameter entries.
                Managers obtain new values for row creation in this table by
                reading diffServTBParamNextFree.
                ''',
                'diffservtbparamid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServTBParamBurstSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The maximum number of bytes in a single transmission burst. This
                attribute is used for:
                1. CBS and EBS in RFC 2697 for srTCM
                2. CBS and PBS in RFC 2698 for trTCM
                3. Burst Size in RFC 3290.
                ''',
                'diffservtbparamburstsize',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServTBParamInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The time interval used with the token bucket.  For:
                1. Average Rate Meter, the Informal Differentiated Services Model
                   section 5.2.1, - Delta.
                2. Simple Token Bucket Meter, the Informal Differentiated
                   Services Model section 5.1, - time interval t.
                3. RFC 2859 TSWTCM, - AVG_INTERVAL.
                4. RFC 2697 srTCM, RFC 2698 trTCM, - token bucket update time
                   interval.
                ''',
                'diffservtbparaminterval',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServTBParamRate', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The token-bucket rate, in kilobits per second (kbps). This
                attribute is used for:
                1. CIR in RFC 2697 for srTCM
                2. CIR and PIR in RFC 2698 for trTCM
                3. CTR and PTR in RFC 2859 for TSWTCM
                4. AverageRate in RFC 3290.
                ''',
                'diffservtbparamrate',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServTBParamStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservtbparamstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServTBParamStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservtbparamstorage',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServTBParamType', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The Metering algorithm associated with the Token Bucket
                parameters.  zeroDotZero indicates this is unknown.
                
                Standard values for generic algorithms:
                diffServTBParamSimpleTokenBucket, diffServTBParamAvgRate,
                diffServTBParamSrTCMBlind, diffServTBParamSrTCMAware,
                diffServTBParamTrTCMBlind, diffServTBParamTrTCMAware, and
                diffServTBParamTswTCM are specified in this MIB as OBJECT-
                IDENTITYs; additional values may be further specified in other
                MIBs.
                ''',
                'diffservtbparamtype',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServTBParamEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservtbparamtable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservtbparamtable',
            False, 
            [
            _MetaInfoClassMember('diffServTBParamEntry', REFERENCE_LIST, 'Diffservtbparamentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservtbparamtable.Diffservtbparamentry', 
                [], [], 
                '''                An entry that describes a single set of token bucket
                parameters.
                ''',
                'diffservtbparamentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServTBParamTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservactiontable.Diffservactionentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservactiontable.Diffservactionentry',
            False, 
            [
            _MetaInfoClassMember('diffServActionId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Action entries.  Managers obtain
                new values for row creation in this table by reading
                diffServActionNextFree.
                ''',
                'diffservactionid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServActionInterface', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The interface index (value of ifIndex) that this action occurs
                on. This may be derived from the diffServDataPathStartEntry's
                index by extension through the various RowPointers. However, as
                this may be difficult for a network management station, it is
                placed here as well.  If this is indeterminate, the value is
                zero.
                
                This is of especial relevance when reporting the counters which
                may apply to traffic crossing an interface:
                   diffServCountActOctets,
                   diffServCountActPkts,
                   diffServAlgDropOctets,
                   diffServAlgDropPkts,
                   diffServAlgRandomDropOctets, and
                   diffServAlgRandomDropPkts.
                
                It is also especially relevant to the queue and scheduler which
                may be subsequently applied.
                ''',
                'diffservactioninterface',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServActionNext', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This selects the next Differentiated Services Functional Data
                Path Element to handle traffic for this data path. This
                RowPointer should point to an instance of one of:
                  diffServClfrEntry
                  diffServMeterEntry
                  diffServActionEntry
                  diffServAlgDropEntry
                  diffServQEntry
                
                A value of zeroDotZero in this attribute indicates no further
                Differentiated Services treatment is performed on traffic of this
                data path. The use of zeroDotZero is the normal usage for the
                last functional data path element of the current data path.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservactionnext',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServActionSpecific', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A pointer to an object instance providing additional information
                for the type of action indicated by this action table entry.
                
                For the standard actions defined by this MIB module, this should
                point to either a diffServDscpMarkActEntry or a
                diffServCountActEntry. For other actions, it may point to an
                object instance defined in some other MIB.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the Meter should be treated as
                if it were not present.  This may lead to incorrect policy
                behavior.
                ''',
                'diffservactionspecific',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServActionStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservactionstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServActionStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservactionstorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServActionEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservactiontable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservactiontable',
            False, 
            [
            _MetaInfoClassMember('diffServActionEntry', REFERENCE_LIST, 'Diffservactionentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservactiontable.Diffservactionentry', 
                [], [], 
                '''                Each entry in the action table allows description of one
                specific action to be applied to traffic.
                ''',
                'diffservactionentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServActionTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry',
            False, 
            [
            _MetaInfoClassMember('diffServDscpMarkActDscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The DSCP that this Action will store into the DSCP field of the
                subject. It is quite possible that the only packets subject to
                this Action are already marked with this DSCP. Note also that
                Differentiated Services processing may result in packet being
                marked on both ingress to a network and on egress from it, and
                that ingress and egress can occur in the same router.
                ''',
                'diffservdscpmarkactdscp',
                'DIFFSERV-MIB', True),
            ],
            'DIFFSERV-MIB',
            'diffServDscpMarkActEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservdscpmarkacttable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservdscpmarkacttable',
            False, 
            [
            _MetaInfoClassMember('diffServDscpMarkActEntry', REFERENCE_LIST, 'Diffservdscpmarkactentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry', 
                [], [], 
                '''                An entry in the DSCP mark action table that describes a single
                DSCP used for marking.
                ''',
                'diffservdscpmarkactentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServDscpMarkActTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservcountacttable.Diffservcountactentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservcountacttable.Diffservcountactentry',
            False, 
            [
            _MetaInfoClassMember('diffServCountActId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Count Action entries.  Managers
                obtain new values for row creation in this table by reading
                
                
                
                diffServCountActNextFree.
                ''',
                'diffservcountactid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServCountActOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets at the Action data path element.
                
                Discontinuities in the value of this counter can occur at re-
                initialization of the management system and at other times as
                indicated by the value of ifCounterDiscontinuityTime on the
                relevant interface.
                ''',
                'diffservcountactoctets',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServCountActPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets at the Action data path element.
                
                Discontinuities in the value of this counter can occur at re-
                initialization of the management system and at other times as
                indicated by the value of ifCounterDiscontinuityTime on the
                relevant interface.
                ''',
                'diffservcountactpkts',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServCountActStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                
                
                
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservcountactstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServCountActStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservcountactstorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServCountActEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservcountacttable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservcountacttable',
            False, 
            [
            _MetaInfoClassMember('diffServCountActEntry', REFERENCE_LIST, 'Diffservcountactentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservcountacttable.Diffservcountactentry', 
                [], [], 
                '''                An entry in the count action table describes a single set of
                traffic counters.
                ''',
                'diffservcountactentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServCountActTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservalgdroptable.Diffservalgdropentry.DiffservalgdroptypeEnum' : _MetaInfoEnum('DiffservalgdroptypeEnum', 'ydk.models.cisco_ios_xe.DIFFSERV_MIB',
        {
            'other':'other',
            'tailDrop':'tailDrop',
            'headDrop':'headDrop',
            'randomDrop':'randomDrop',
            'alwaysDrop':'alwaysDrop',
        }, 'DIFFSERV-MIB', _yang_ns._namespaces['DIFFSERV-MIB']),
    'DiffservMib.Diffservalgdroptable.Diffservalgdropentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservalgdroptable.Diffservalgdropentry',
            False, 
            [
            _MetaInfoClassMember('diffServAlgDropId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Algorithmic Dropper entries.
                Managers obtain new values for row creation in this table by
                reading diffServAlgDropNextFree.
                ''',
                'diffservalgdropid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServAlgDropNext', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This selects the next Differentiated Services Functional Data
                Path Element to handle traffic for this data path. This
                RowPointer should point to an instance of one of:
                  diffServClfrEntry
                  diffServMeterEntry
                  diffServActionEntry
                  diffServQEntry
                
                A value of zeroDotZero in this attribute indicates no further
                Differentiated Services treatment is performed on traffic of this
                data path. The use of zeroDotZero is the normal usage for the
                last functional data path element of the current data path.
                
                When diffServAlgDropType is alwaysDrop(5), this object is
                ignored.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservalgdropnext',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets that have been deterministically dropped by
                this drop process.
                
                Discontinuities in the value of this counter can occur at re-
                initialization of the management system and at other times as
                indicated by the value of ifCounterDiscontinuityTime on the
                relevant interface.
                ''',
                'diffservalgdropoctets',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets that have been deterministically dropped
                by this drop process.
                
                Discontinuities in the value of this counter can occur at re-
                initialization of the management system and at other times as
                indicated by the value of ifCounterDiscontinuityTime on the
                relevant interface.
                ''',
                'diffservalgdroppkts',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropQMeasure', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Points to an entry in the diffServQTable to indicate the queue
                that a drop algorithm is to monitor when deciding whether to drop
                a packet. If the row pointed to does not exist, the algorithmic
                dropper element is considered inactive.
                
                
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservalgdropqmeasure',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropQThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A threshold on the depth in bytes of the queue being measured at
                which a trigger is generated to the dropping algorithm, unless
                diffServAlgDropType is alwaysDrop(5) where this object is
                ignored.
                
                For the tailDrop(2) or headDrop(3) algorithms, this represents
                the depth of the queue, pointed to by diffServAlgDropQMeasure, at
                which the drop action will take place. Other algorithms will need
                to define their own semantics for this threshold.
                ''',
                'diffservalgdropqthreshold',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropSpecific', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Points to a table entry that provides further detail regarding a
                drop algorithm.
                
                Entries with diffServAlgDropType equal to other(1) may have this
                point to a table defined in another MIB module.
                
                Entries with diffServAlgDropType equal to randomDrop(4) must have
                this point to an entry in diffServRandomDropTable.
                
                For all other algorithms specified in this MIB, this should take
                the value zeroDotZero.
                
                The diffServAlgDropType is authoritative for the type of the drop
                algorithm and the specific parameters for the drop algorithm
                needs to be evaluated based on the diffServAlgDropType.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservalgdropspecific',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservalgdropstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservalgdropstorage',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropType', REFERENCE_ENUM_CLASS, 'DiffservalgdroptypeEnum' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservalgdroptable.Diffservalgdropentry.DiffservalgdroptypeEnum', 
                [], [], 
                '''                The type of algorithm used by this dropper. The value other(1)
                requires further specification in some other MIB module.
                
                In the tailDrop(2) algorithm, diffServAlgDropQThreshold
                represents the maximum depth of the queue, pointed to by
                diffServAlgDropQMeasure, beyond which all newly arriving packets
                will be dropped.
                
                In the headDrop(3) algorithm, if a packet arrives when the
                current depth of the queue, pointed to by
                diffServAlgDropQMeasure, is at diffServAlgDropQThreshold, packets
                currently at the head of the queue are dropped to make room for
                the new packet to be enqueued at the tail of the queue.
                
                In the randomDrop(4) algorithm, on packet arrival, an Active
                Queue Management algorithm is executed which may randomly drop a
                packet. This algorithm may be proprietary, and it may drop either
                the arriving packet or another packet in the queue.
                diffServAlgDropSpecific points to a diffServRandomDropEntry that
                describes the algorithm. For this algorithm,
                
                
                
                diffServAlgDropQThreshold is understood to be the absolute
                maximum size of the queue and additional parameters are described
                in diffServRandomDropTable.
                
                The alwaysDrop(5) algorithm is as its name specifies; always
                drop. In this case, the other configuration values in this Entry
                are not meaningful; There is no useful 'next' processing step,
                there is no queue, and parameters describing the queue are not
                useful. Therefore, diffServAlgDropNext, diffServAlgDropMeasure,
                and diffServAlgDropSpecific are all zeroDotZero.
                ''',
                'diffservalgdroptype',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgRandomDropOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of octets that have been randomly dropped by this
                drop process.  This counter applies, therefore, only to random
                droppers.
                
                Discontinuities in the value of this counter can occur at re-
                initialization of the management system and at other times as
                indicated by the value of ifCounterDiscontinuityTime on the
                relevant interface.
                ''',
                'diffservalgrandomdropoctets',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgRandomDropPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets that have been randomly dropped by this
                drop process. This counter applies, therefore, only to random
                droppers.
                
                Discontinuities in the value of this counter can occur at re-
                initialization of the management system and at other times as
                indicated by the value of ifCounterDiscontinuityTime on the
                relevant interface.
                ''',
                'diffservalgrandomdroppkts',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServAlgDropEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservalgdroptable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservalgdroptable',
            False, 
            [
            _MetaInfoClassMember('diffServAlgDropEntry', REFERENCE_LIST, 'Diffservalgdropentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservalgdroptable.Diffservalgdropentry', 
                [], [], 
                '''                An entry describes a process that drops packets according to
                some algorithm. Further details of the algorithm type are to be
                found in diffServAlgDropType and with more detail parameter entry
                pointed to by diffServAlgDropSpecific when necessary.
                ''',
                'diffservalgdropentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServAlgDropTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry',
            False, 
            [
            _MetaInfoClassMember('diffServRandomDropId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Random Drop entries.  Managers
                obtain new values for row creation in this table by reading
                diffServRandomDropNextFree.
                ''',
                'diffservrandomdropid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServRandomDropMaxThreshBytes', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The average queue depth beyond which traffic has a probability
                indicated by diffServRandomDropProbMax of being dropped or
                marked. Note that this differs from the physical queue limit,
                which is stored in diffServAlgDropQThreshold. Changes in this
                variable may or may not be reflected in the reported value of
                diffServRandomDropMaxThreshPkts.
                ''',
                'diffservrandomdropmaxthreshbytes',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropMaxThreshPkts', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The average queue depth beyond which traffic has a probability
                indicated by diffServRandomDropProbMax of being dropped or
                marked. Note that this differs from the physical queue limit,
                which is stored in diffServAlgDropQThreshold. Changes in this
                variable may or may not be reflected in the reported value of
                diffServRandomDropMaxThreshBytes.
                ''',
                'diffservrandomdropmaxthreshpkts',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropMinThreshBytes', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The average queue depth in bytes, beyond which traffic has a
                non-zero probability of being dropped. Changes in this variable
                may or may not be reflected in the reported value of
                diffServRandomDropMinThreshPkts.
                ''',
                'diffservrandomdropminthreshbytes',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropMinThreshPkts', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The average queue depth in packets, beyond which traffic has a
                non-zero probability of being dropped. Changes in this variable
                may or may not be reflected in the reported value of
                diffServRandomDropMinThreshBytes.
                ''',
                'diffservrandomdropminthreshpkts',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropProbMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                The worst case random drop probability, expressed in drops per
                thousand packets.
                
                For example, if in the worst case every arriving packet may be
                dropped (100%) for a period, this has the value 1000.
                Alternatively, if in the worst case only one percent (1%) of
                traffic may be dropped, it has the value 10.
                ''',
                'diffservrandomdropprobmax',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropSamplingRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000000')], [], 
                '''                The number of times per second the queue is sampled for queue
                average calculation.  A value of zero is used to mean that the
                queue is sampled approximately each time a packet is enqueued (or
                dequeued).
                ''',
                'diffservrandomdropsamplingrate',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservrandomdropstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservrandomdropstorage',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropWeight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The weighting of past history in affecting the Exponentially
                Weighted Moving Average function that calculates the current
                average queue depth.  The equation uses
                diffServRandomDropWeight/65536 as the coefficient for the new
                sample in the equation, and (65536 -
                diffServRandomDropWeight)/65536 as the coefficient of the old
                value.
                
                Implementations may limit the values of diffServRandomDropWeight
                to a subset of the possible range of values, such as powers of
                two. Doing this would facilitate implementation of the
                Exponentially Weighted Moving Average using shift instructions or
                registers.
                ''',
                'diffservrandomdropweight',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServRandomDropEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservrandomdroptable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservrandomdroptable',
            False, 
            [
            _MetaInfoClassMember('diffServRandomDropEntry', REFERENCE_LIST, 'Diffservrandomdropentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry', 
                [], [], 
                '''                An entry describes a process that drops packets according to a
                random algorithm.
                ''',
                'diffservrandomdropentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServRandomDropTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservqtable.Diffservqentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservqtable.Diffservqentry',
            False, 
            [
            _MetaInfoClassMember('diffServQId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Queue entries.  Managers obtain new
                values for row creation in this table by reading
                diffServQNextFree.
                ''',
                'diffservqid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServQMaxRate', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This RowPointer indicates the diffServMaxRateEntry that the
                scheduler, pointed to by diffServQNext, should use to service
                this queue.
                
                If the row pointed to is zeroDotZero, the maximum rate is the
                line speed of the interface.
                
                
                
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservqmaxrate',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServQMinRate', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This RowPointer indicates the diffServMinRateEntry that the
                scheduler, pointed to by diffServQNext, should use to service
                this queue.
                
                If the row pointed to is zeroDotZero, the minimum rate and
                priority is unspecified.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservqminrate',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServQNext', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This selects the next Differentiated Services Scheduler.  The
                RowPointer must point to a diffServSchedulerEntry.
                
                A value of zeroDotZero in this attribute indicates an incomplete
                diffServQEntry instance. In such a case, the entry has no
                operational effect, since it has no parameters to give it
                meaning.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservqnext',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServQStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservqstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServQStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservqstorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServQEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservqtable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservqtable',
            False, 
            [
            _MetaInfoClassMember('diffServQEntry', REFERENCE_LIST, 'Diffservqentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservqtable.Diffservqentry', 
                [], [], 
                '''                An entry in the Queue Table describes a single queue or class of
                traffic.
                ''',
                'diffservqentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServQTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservschedulertable.Diffservschedulerentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservschedulertable.Diffservschedulerentry',
            False, 
            [
            _MetaInfoClassMember('diffServSchedulerId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Scheduler entries.  Managers obtain
                new values for row creation in this table by reading
                diffServSchedulerNextFree.
                ''',
                'diffservschedulerid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServSchedulerMaxRate', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This RowPointer indicates the entry in diffServMaxRateTable
                which indicates the maximum output rate from this scheduler.
                When more than one maximum rate applies (eg, when a multi-rate
                shaper is in view), it points to the first of those rate entries.
                This attribute is used only when there is more than one level of
                scheduler.
                
                When it has the value zeroDotZero, it indicates that no maximum
                rate is imposed.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservschedulermaxrate',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServSchedulerMethod', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The scheduling algorithm used by this Scheduler. zeroDotZero
                indicates that this is unknown.  Standard values for generic
                algorithms: diffServSchedulerPriority, diffServSchedulerWRR, and
                diffServSchedulerWFQ are specified in this MIB; additional values
                
                
                
                may be further specified in other MIBs.
                ''',
                'diffservschedulermethod',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServSchedulerMinRate', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This RowPointer indicates the entry in diffServMinRateTable
                which indicates the priority or minimum output rate from this
                scheduler. This attribute is used only when there is more than
                one level of scheduler.
                
                When it has the value zeroDotZero, it indicates that no minimum
                rate or priority is imposed.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservschedulerminrate',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServSchedulerNext', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This selects the next Differentiated Services Functional Data
                Path Element to handle traffic for this data path. This normally
                is null (zeroDotZero), or points to a diffServSchedulerEntry or a
                diffServQEntry.
                
                However, this RowPointer may also point to an instance of:
                  diffServClfrEntry,
                  diffServMeterEntry,
                  diffServActionEntry,
                  diffServAlgDropEntry.
                
                It would point another diffServSchedulerEntry when implementing
                multiple scheduler methods for the same data path, such as having
                one set of queues scheduled by WRR and that group participating
                in a priority scheduling system in which other queues compete
                with it in that way.  It might also point to a second scheduler
                in a hierarchical scheduling system.
                
                If the row pointed to is zeroDotZero, no further Differentiated
                Services treatment is performed on traffic of this data path.
                
                Setting this to point to a target that does not exist results in
                an inconsistentValue error.  If the row pointed to is removed or
                becomes inactive by other means, the treatment is as if this
                attribute contains a value of zeroDotZero.
                ''',
                'diffservschedulernext',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServSchedulerStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservschedulerstatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServSchedulerStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservschedulerstorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServSchedulerEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservschedulertable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservschedulertable',
            False, 
            [
            _MetaInfoClassMember('diffServSchedulerEntry', REFERENCE_LIST, 'Diffservschedulerentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservschedulertable.Diffservschedulerentry', 
                [], [], 
                '''                An entry in the Scheduler Table describing a single instance of
                a scheduling algorithm.
                ''',
                'diffservschedulerentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServSchedulerTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservminratetable.Diffservminrateentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservminratetable.Diffservminrateentry',
            False, 
            [
            _MetaInfoClassMember('diffServMinRateId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Scheduler Parameter entries.
                Managers obtain new values for row creation in this table by
                reading diffServMinRateNextFree.
                ''',
                'diffservminrateid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServMinRateAbsolute', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The minimum absolute rate, in kilobits/sec, that a downstream
                scheduler element should allocate to this queue. If the value is
                zero, then there is effectively no minimum rate guarantee. If the
                value is non-zero, the scheduler will assure the servicing of
                this queue to at least this rate.
                
                Note that this attribute value and that of
                diffServMinRateRelative are coupled: changes to one will affect
                the value of the other. They are linked by the following
                equation, in that setting one will change the other:
                
                  diffServMinRateRelative =
                          (diffServMinRateAbsolute*1000000)/ifSpeed
                
                or, if appropriate:
                
                  diffServMinRateRelative = diffServMinRateAbsolute/ifHighSpeed
                ''',
                'diffservminrateabsolute',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMinRatePriority', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The priority of this input to the associated scheduler, relative
                
                
                
                to the scheduler's other inputs. A queue or scheduler with a
                larger numeric value will be served before another with a smaller
                numeric value.
                ''',
                'diffservminratepriority',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMinRateRelative', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The minimum rate that a downstream scheduler element should
                allocate to this queue, relative to the maximum rate of the
                interface as reported by ifSpeed or ifHighSpeed, in units of
                1/1000 of 1. If the value is zero, then there is effectively no
                minimum rate guarantee. If the value is non-zero, the scheduler
                will assure the servicing of this queue to at least this rate.
                
                Note that this attribute value and that of
                diffServMinRateAbsolute are coupled: changes to one will affect
                the value of the other. They are linked by the following
                equation, in that setting one will change the other:
                
                
                
                  diffServMinRateRelative =
                          (diffServMinRateAbsolute*1000000)/ifSpeed
                
                or, if appropriate:
                
                  diffServMinRateRelative = diffServMinRateAbsolute/ifHighSpeed
                ''',
                'diffservminraterelative',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMinRateStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservminratestatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMinRateStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservminratestorage',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMinRateEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservminratetable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservminratetable',
            False, 
            [
            _MetaInfoClassMember('diffServMinRateEntry', REFERENCE_LIST, 'Diffservminrateentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservminratetable.Diffservminrateentry', 
                [], [], 
                '''                An entry in the Minimum Rate Parameters Table describes a single
                set of scheduling parameters for use by one or more queues or
                schedulers.
                ''',
                'diffservminrateentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMinRateTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservmaxratetable.Diffservmaxrateentry' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservmaxratetable.Diffservmaxrateentry',
            False, 
            [
            _MetaInfoClassMember('diffServMaxRateId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index that enumerates the Maximum Rate Parameter entries.
                Managers obtain new values for row creation in this table by
                reading diffServMaxRateNextFree.
                ''',
                'diffservmaxrateid',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServMaxRateLevel', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                An index that indicates which level of a multi-rate shaper is
                being given its parameters. A multi-rate shaper has some number
                of rate levels. Frame Relay's dual rate specification refers to a
                'committed' and an 'excess' rate; ATM's dual rate specification
                refers to a 'mean' and a 'peak' rate. This table is generalized
                to support an arbitrary number of rates. The committed or mean
                rate is level 1, the peak rate (if any) is the highest level rate
                configured, and if there are other rates they are distributed in
                monotonically increasing order between them.
                ''',
                'diffservmaxratelevel',
                'DIFFSERV-MIB', True),
            _MetaInfoClassMember('diffServMaxRateAbsolute', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The maximum rate in kilobits/sec that a downstream scheduler
                element should allocate to this queue. If the value is zero, then
                there is effectively no maximum rate limit and that the scheduler
                should attempt to be work conserving for this queue. If the value
                is non-zero, the scheduler will limit the servicing of this queue
                to, at most, this rate in a non-work-conserving manner.
                
                Note that this attribute value and that of
                diffServMaxRateRelative are coupled: changes to one will affect
                the value of the other. They are linked by the following
                
                
                
                equation, in that setting one will change the other:
                
                  diffServMaxRateRelative =
                          (diffServMaxRateAbsolute*1000000)/ifSpeed
                
                or, if appropriate:
                
                  diffServMaxRateRelative = diffServMaxRateAbsolute/ifHighSpeed
                ''',
                'diffservmaxrateabsolute',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMaxRateRelative', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The maximum rate that a downstream scheduler element should
                allocate to this queue, relative to the maximum rate of the
                interface as reported by ifSpeed or ifHighSpeed, in units of
                1/1000 of 1. If the value is zero, then there is effectively no
                maximum rate limit and the scheduler should attempt to be work
                conserving for this queue. If the value is non-zero, the
                scheduler will limit the servicing of this queue to, at most,
                this rate in a non-work-conserving manner.
                
                Note that this attribute value and that of
                diffServMaxRateAbsolute are coupled: changes to one will affect
                the value of the other. They are linked by the following
                equation, in that setting one will change the other:
                
                  diffServMaxRateRelative =
                          (diffServMaxRateAbsolute*1000000)/ifSpeed
                
                or, if appropriate:
                
                  diffServMaxRateRelative = diffServMaxRateAbsolute/ifHighSpeed
                ''',
                'diffservmaxraterelative',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMaxRateStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row. All writable objects in this
                row may be modified at any time. Setting this variable to
                'destroy' when the MIB contains one or more RowPointers pointing
                to it results in destruction being delayed until the row is no
                longer used.
                ''',
                'diffservmaxratestatus',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMaxRateStorage', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.  Conceptual rows
                having the value 'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'diffservmaxratestorage',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMaxRateThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of bytes of queue depth at which the rate of a
                
                
                
                multi-rate scheduler will increase to the next output rate. In
                the last conceptual row for such a shaper, this threshold is
                ignored and by convention is zero.
                ''',
                'diffservmaxratethreshold',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMaxRateEntry',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib.Diffservmaxratetable' : {
        'meta_info' : _MetaInfoClass('DiffservMib.Diffservmaxratetable',
            False, 
            [
            _MetaInfoClassMember('diffServMaxRateEntry', REFERENCE_LIST, 'Diffservmaxrateentry' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservmaxratetable.Diffservmaxrateentry', 
                [], [], 
                '''                An entry in the Maximum Rate Parameter Table describes a single
                set of scheduling parameters for use by one or more queues or
                schedulers.
                ''',
                'diffservmaxrateentry',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'diffServMaxRateTable',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
    'DiffservMib' : {
        'meta_info' : _MetaInfoClass('DiffservMib',
            False, 
            [
            _MetaInfoClassMember('diffServAction', REFERENCE_CLASS, 'Diffservaction' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservaction', 
                [], [], 
                '''                ''',
                'diffservaction',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServActionTable', REFERENCE_CLASS, 'Diffservactiontable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservactiontable', 
                [], [], 
                '''                The Action Table enumerates actions that can be performed to a
                stream of traffic. Multiple actions can be concatenated. For
                example, traffic exiting from a meter may be counted, marked, and
                potentially dropped before entering a queue.
                
                Specific actions are indicated by diffServActionSpecific which
                points to an entry of a specific action type parameterizing the
                action in detail.
                ''',
                'diffservactiontable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDrop', REFERENCE_CLASS, 'Diffservalgdrop' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservalgdrop', 
                [], [], 
                '''                ''',
                'diffservalgdrop',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServAlgDropTable', REFERENCE_CLASS, 'Diffservalgdroptable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservalgdroptable', 
                [], [], 
                '''                The algorithmic drop table contains entries describing an
                element that drops packets according to some algorithm.
                ''',
                'diffservalgdroptable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClassifier', REFERENCE_CLASS, 'Diffservclassifier' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservclassifier', 
                [], [], 
                '''                ''',
                'diffservclassifier',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClfrElementTable', REFERENCE_CLASS, 'Diffservclfrelementtable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservclfrelementtable', 
                [], [], 
                '''                The classifier element table enumerates the relationship between
                classification patterns and subsequent downstream Differentiated
                Services Functional Data Path elements.
                diffServClfrElementSpecific points to a filter that specifies the
                classification parameters. A classifier may use filter tables of
                different types together.
                
                One example of a filter table defined in this MIB is
                diffServMultiFieldClfrTable, for IP Multi-Field Classifiers
                (MFCs). Such an entry might identify anything from a single
                micro-flow (an identifiable sub-session packet stream directed
                from one sending transport to the receiving transport or
                transports), or aggregates of those such as the traffic from a
                host, traffic for an application, or traffic between two hosts
                using an application and a given DSCP. The standard Behavior
                Aggregate used in the Differentiated Services Architecture is
                encoded as a degenerate case of such an aggregate - the traffic
                using a particular DSCP value.
                
                Filter tables for other filter types may be defined elsewhere.
                ''',
                'diffservclfrelementtable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServClfrTable', REFERENCE_CLASS, 'Diffservclfrtable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservclfrtable', 
                [], [], 
                '''                This table enumerates all the diffserv classifier functional
                data path elements of this device.  The actual classification
                definitions are defined in diffServClfrElementTable entries
                belonging to each classifier.
                
                An entry in this table, pointed to by a RowPointer specifying an
                instance of diffServClfrStatus, is frequently used as the name
                for a set of classifier elements, which all use the index
                diffServClfrId. Per the semantics of the classifier element
                table, these entries constitute one or more unordered sets of
                tests which may be simultaneously applied to a message to
                
                
                
                classify it.
                
                The primary function of this table is to ensure that the value of
                diffServClfrId is unique before attempting to use it in creating
                a diffServClfrElementEntry. Therefore, the diffServClfrEntry must
                be created on the same SET as the diffServClfrElementEntry, or
                before the diffServClfrElementEntry is created.
                ''',
                'diffservclfrtable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServCountActTable', REFERENCE_CLASS, 'Diffservcountacttable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservcountacttable', 
                [], [], 
                '''                This table contains counters for all the traffic passing through
                an action element.
                ''',
                'diffservcountacttable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServDataPathTable', REFERENCE_CLASS, 'Diffservdatapathtable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservdatapathtable', 
                [], [], 
                '''                The data path table contains RowPointers indicating the start of
                the functional data path for each interface and traffic direction
                in this device. These may merge, or be separated into parallel
                data paths.
                ''',
                'diffservdatapathtable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServDscpMarkActTable', REFERENCE_CLASS, 'Diffservdscpmarkacttable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservdscpmarkacttable', 
                [], [], 
                '''                This table enumerates specific DSCPs used for marking or
                remarking the DSCP field of IP packets. The entries of this table
                may be referenced by a diffServActionSpecific attribute.
                ''',
                'diffservdscpmarkacttable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMaxRateTable', REFERENCE_CLASS, 'Diffservmaxratetable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservmaxratetable', 
                [], [], 
                '''                The Maximum Rate Parameter Table enumerates individual sets of
                scheduling parameter that can be used/reused by Queues and
                Schedulers.
                ''',
                'diffservmaxratetable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMeter', REFERENCE_CLASS, 'Diffservmeter' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservmeter', 
                [], [], 
                '''                ''',
                'diffservmeter',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMeterTable', REFERENCE_CLASS, 'Diffservmetertable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservmetertable', 
                [], [], 
                '''                This table enumerates specific meters that a system may use to
                police a stream of traffic. The traffic stream to be metered is
                determined by the Differentiated Services Functional Data Path
                Element(s) upstream of the meter i.e. by the object(s) that point
                to each entry in this table.  This may include all traffic on an
                interface.
                
                Specific meter details are to be found in table entry referenced
                by diffServMeterSpecific.
                ''',
                'diffservmetertable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMinRateTable', REFERENCE_CLASS, 'Diffservminratetable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservminratetable', 
                [], [], 
                '''                The Minimum Rate Parameters Table enumerates individual sets of
                scheduling parameter that can be used/reused by Queues and
                Schedulers.
                ''',
                'diffservminratetable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServMultiFieldClfrTable', REFERENCE_CLASS, 'Diffservmultifieldclfrtable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservmultifieldclfrtable', 
                [], [], 
                '''                A table of IP Multi-field Classifier filter entries that a
                
                
                
                system may use to identify IP traffic.
                ''',
                'diffservmultifieldclfrtable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServQTable', REFERENCE_CLASS, 'Diffservqtable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservqtable', 
                [], [], 
                '''                The Queue Table enumerates the individual queues.  Note that the
                MIB models queuing systems as composed of individual queues, one
                per class of traffic, even though they may in fact be structured
                as classes of traffic scheduled using a common calendar queue, or
                in other ways.
                ''',
                'diffservqtable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServQueue', REFERENCE_CLASS, 'Diffservqueue' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservqueue', 
                [], [], 
                '''                ''',
                'diffservqueue',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServRandomDropTable', REFERENCE_CLASS, 'Diffservrandomdroptable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservrandomdroptable', 
                [], [], 
                '''                The random drop table contains entries describing a process that
                drops packets randomly. Entries in this table are pointed to by
                diffServAlgDropSpecific.
                ''',
                'diffservrandomdroptable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServScheduler', REFERENCE_CLASS, 'Diffservscheduler' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservscheduler', 
                [], [], 
                '''                ''',
                'diffservscheduler',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServSchedulerTable', REFERENCE_CLASS, 'Diffservschedulertable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservschedulertable', 
                [], [], 
                '''                The Scheduler Table enumerates packet schedulers. Multiple
                scheduling algorithms can be used on a given data path, with each
                algorithm described by one diffServSchedulerEntry.
                ''',
                'diffservschedulertable',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServTBParam', REFERENCE_CLASS, 'Diffservtbparam' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservtbparam', 
                [], [], 
                '''                ''',
                'diffservtbparam',
                'DIFFSERV-MIB', False),
            _MetaInfoClassMember('diffServTBParamTable', REFERENCE_CLASS, 'Diffservtbparamtable' , 'ydk.models.cisco_ios_xe.DIFFSERV_MIB', 'DiffservMib.Diffservtbparamtable', 
                [], [], 
                '''                This table enumerates a single set of token bucket meter
                parameters that a system may use to police a stream of traffic.
                Such meters are modeled here as having a single rate and a single
                burst size. Multiple entries are used when multiple rates/burst
                sizes are needed.
                ''',
                'diffservtbparamtable',
                'DIFFSERV-MIB', False),
            ],
            'DIFFSERV-MIB',
            'DIFFSERV-MIB',
            _yang_ns._namespaces['DIFFSERV-MIB'],
        'ydk.models.cisco_ios_xe.DIFFSERV_MIB'
        ),
    },
}
_meta_table['DiffservMib.Diffservdatapathtable.Diffservdatapathentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservdatapathtable']['meta_info']
_meta_table['DiffservMib.Diffservclfrtable.Diffservclfrentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservclfrtable']['meta_info']
_meta_table['DiffservMib.Diffservclfrelementtable.Diffservclfrelemententry']['meta_info'].parent =_meta_table['DiffservMib.Diffservclfrelementtable']['meta_info']
_meta_table['DiffservMib.Diffservmultifieldclfrtable.Diffservmultifieldclfrentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservmultifieldclfrtable']['meta_info']
_meta_table['DiffservMib.Diffservmetertable.Diffservmeterentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservmetertable']['meta_info']
_meta_table['DiffservMib.Diffservtbparamtable.Diffservtbparamentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservtbparamtable']['meta_info']
_meta_table['DiffservMib.Diffservactiontable.Diffservactionentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservactiontable']['meta_info']
_meta_table['DiffservMib.Diffservdscpmarkacttable.Diffservdscpmarkactentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservdscpmarkacttable']['meta_info']
_meta_table['DiffservMib.Diffservcountacttable.Diffservcountactentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservcountacttable']['meta_info']
_meta_table['DiffservMib.Diffservalgdroptable.Diffservalgdropentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservalgdroptable']['meta_info']
_meta_table['DiffservMib.Diffservrandomdroptable.Diffservrandomdropentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservrandomdroptable']['meta_info']
_meta_table['DiffservMib.Diffservqtable.Diffservqentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservqtable']['meta_info']
_meta_table['DiffservMib.Diffservschedulertable.Diffservschedulerentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservschedulertable']['meta_info']
_meta_table['DiffservMib.Diffservminratetable.Diffservminrateentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservminratetable']['meta_info']
_meta_table['DiffservMib.Diffservmaxratetable.Diffservmaxrateentry']['meta_info'].parent =_meta_table['DiffservMib.Diffservmaxratetable']['meta_info']
_meta_table['DiffservMib.Diffservclassifier']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservmeter']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservtbparam']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservaction']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservalgdrop']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservqueue']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservscheduler']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservdatapathtable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservclfrtable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservclfrelementtable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservmultifieldclfrtable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservmetertable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservtbparamtable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservactiontable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservdscpmarkacttable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservcountacttable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservalgdroptable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservrandomdroptable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservqtable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservschedulertable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservminratetable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
_meta_table['DiffservMib.Diffservmaxratetable']['meta_info'].parent =_meta_table['DiffservMib']['meta_info']
