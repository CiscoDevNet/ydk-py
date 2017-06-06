


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CatmoamrecoverytypeEnum' : _MetaInfoEnum('CatmoamrecoverytypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB',
        {
            'catmLoopbackOAMRecover':'catmLoopbackOAMRecover',
            'catmSegmentCCOAMRecover':'catmSegmentCCOAMRecover',
            'catmEndCCOAMRecover':'catmEndCCOAMRecover',
            'catmAISRDIOAMRecover':'catmAISRDIOAMRecover',
        }, 'CISCO-ATM-PVCTRAP-EXTN-MIB', _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB']),
    'CatmoamfailuretypeEnum' : _MetaInfoEnum('CatmoamfailuretypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB',
        {
            'catmLoopbackOAMFailure':'catmLoopbackOAMFailure',
            'catmSegmentCCOAMFailure':'catmSegmentCCOAMFailure',
            'catmEndCCOAMFailure':'catmEndCCOAMFailure',
            'catmAISRDIOAMFailure':'catmAISRDIOAMFailure',
        }, 'CISCO-ATM-PVCTRAP-EXTN-MIB', _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB']),
    'CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclAISRDIStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification due
                to AIS RDI OAM failure.
                ''',
                'catmpvclaisrdistatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last corresponding notification due
                to AIS RDI OAM failure.
                ''',
                'catmpvclaisrdistatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last corresponding notification due
                to AIS RDI OAM failure.
                ''',
                'catmpvclaisrdistatustransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclCurFailTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to DOWN
                last time in the last corresponding notification .
                ''',
                'catmpvclcurfailtime',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification due
                to End CC OAM failure.
                ''',
                'catmpvclendccstatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last corresponding notification due
                to End CC OAM failure.
                ''',
                'catmpvclendccstatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last corresponding notification due
                to End CC OAM failure.
                ''',
                'catmpvclendccstatustransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclFailureReason', REFERENCE_ENUM_CLASS, 'CatmoamfailuretypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmoamfailuretypeEnum', 
                [], [], 
                '''                Type of OAM failure.
                ''',
                'catmpvclfailurereason',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclPrevRecoverTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to UP
                last time in the previous corresponding notification .
                ''',
                'catmpvclprevrecovertime',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification due
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccstatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last corresponding notification due
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccstatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last corresponding notification due
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccstatustransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification.
                ''',
                'catmpvclstatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last corresponding notification.
                ''',
                'catmpvclstatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last corresponding notification.
                ''',
                'catmpvclstatustransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmCurStatChangePVclEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable',
            False, 
            [
            _MetaInfoClassMember('catmCurStatChangePVclEntry', REFERENCE_LIST, 'Catmcurstatchangepvclentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry', 
                [], [], 
                '''                Each entry in the table represents a VCL for which
                there is an active row in the atmVclTable having an
                atmVclConnKind value of `pvc' and atmVclOperStatus
                to have changed in the last corresponding PVC notification.
                ''',
                'catmcurstatchangepvclentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmCurStatChangePVclTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Index to represent different ranges, the first range is
                indexed by value 0, the second by 1 and so on...
                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmOperStatus to have changed in the last 
                corresponding notification due to Loopback OAM failure.
                ''',
                'catmpvclhigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus to have changed in the last 
                corresponding notification due to Loopback OAM failure.
                ''',
                'catmpvcllowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last corresponding notification due 
                to Loopback OAM failure.
                ''',
                'catmpvclrangestatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first PVCL in the range
                changed state in the last corresponding notification due 
                to Loopback OAM failure.
                ''',
                'catmpvclrangestatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmStatusChangePVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmStatusChangePVclRangeEntry', REFERENCE_LIST, 'Catmstatuschangepvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and 
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
                changed in the same direction in the last notification 
                interval.
                ''',
                'catmstatuschangepvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmStatusChangePVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclSegCCHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmOperStatus to have changed in the last 
                corresponding notification due to Segment CC OAM failure.
                ''',
                'catmpvclsegcchigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus to have changed in the last 
                corresponding notification due to Segment CC OAM failure.
                ''',
                'catmpvclsegcclowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCRangeStatusChEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last corresponding notification due 
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccrangestatuschend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCRangeStatusChStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first PVCL in the range
                changed state in the last corresponding notification due 
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccrangestatuschstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmSegCCStatusChPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmSegCCStatusChPVclRangeEntry', REFERENCE_LIST, 'Catmsegccstatuschpvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and 
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
                changed due to segment CC failure in the same direction 
                in the last corresponding notification .
                ''',
                'catmsegccstatuschpvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmSegCCStatusChPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclEndCCHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmOperStatus to have changed in the last 
                corresponding notification due to End CC OAM failure.
                ''',
                'catmpvclendcchigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus to have changed in the last 
                corresponding notification due to End CC OAM failure.
                ''',
                'catmpvclendcclowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCRangeStatusChEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last corresponding notification due 
                to End CC OAM failure.
                ''',
                'catmpvclendccrangestatuschend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCRangeStatusChStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first PVCL in the range
                changed state in the last corresponding notification due 
                to End CC OAM failure.
                ''',
                'catmpvclendccrangestatuschstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmEndCCStatusChPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmEndCCStatusChPVclRangeEntry', REFERENCE_LIST, 'Catmendccstatuschpvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and 
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
                changed due to End CC failure in the same direction in the 
                last corresponding notification .
                ''',
                'catmendccstatuschpvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmEndCCStatusChPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclAISRDIHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmOperStatus to have changed in the last 
                corresponding notification due to AISRDI OAM failure.
                ''',
                'catmpvclaisrdihigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDILowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus to have changed in the last 
                corresponding notification due to AISRDI OAM failure.
                ''',
                'catmpvclaisrdilowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIRangeStatusChEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last corresponding notification due 
                to AISRDI OAM failure.
                ''',
                'catmpvclaisrdirangestatuschend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIRangeStatusChStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first PVCL in the range
                changed state in the last corresponding notification due 
                to AISRDI OAM failure.
                ''',
                'catmpvclaisrdirangestatuschstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmAISRDIStatusChPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmAISRDIStatusChPVclRangeEntry', REFERENCE_LIST, 'Catmaisrdistatuschpvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and 
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
                changed due to AIS/RDI failure in the same direction in the 
                last corresponding notification .
                ''',
                'catmaisrdistatuschpvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmAISRDIStatusChPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmDownPVclHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmVclOperStatus has been detected as Down in the 
                corresponding notification .
                ''',
                'catmdownpvclhigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmDownPVclLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus has been detected as Down in the 
                corresponding notification .
                ''',
                'catmdownpvcllowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmDownPVclRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last atmVclOperStatus
                is detected as Down on any of the PVCLs in the range
                in the corresponding notification .
                ''',
                'catmdownpvclrangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmDownPVclRangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first atmVclOperStatus
                is detected as Down on any of the PVCLs in the range
                in the corresponding notification .
                ''',
                'catmdownpvclrangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPrevUpPVclRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last atmVclOperStatus
                is detected as Up on any of the PVCLs in the range
                in the previous catmIntfPvcUp2Trap notification.
                ''',
                'catmprevuppvclrangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPrevUpPVclRangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first atmVclOperStatus
                is detected as Up on any of the PVCLs in the range
                in the previous catmIntfPvcUp2Trap notification.
                ''',
                'catmprevuppvclrangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeFailureReason', REFERENCE_ENUM_CLASS, 'CatmoamfailuretypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmoamfailuretypeEnum', 
                [], [], 
                '''                Type of OAM failure.
                ''',
                'catmpvclrangefailurereason',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmDownPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmDownPVclRangeEntry', REFERENCE_LIST, 'Catmdownpvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and 
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
                have detected as Down in the last notification 
                interval.
                ''',
                'catmdownpvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmDownPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclAISRDIStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to Up
                for the last time in the last corresponding notification 
                due to AIS/RDI OAM recovery.
                ''',
                'catmpvclaisrdistatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to Up
                for the first time in the last corresponding notification 
                due to AIS/RDI OAM recovery.
                ''',
                'catmpvclaisrdistatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIStatusUpTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Down to Up state transitions that 
                has happened on this PVCL in the last notification 
                interval due to AIS RDI OAM recovery.
                ''',
                'catmpvclaisrdistatusuptransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclCurRecoverTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to UP
                last time in the last corresponding notification .
                ''',
                'catmpvclcurrecovertime',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to Up
                for the last time in the last corresponding notification 
                due to End CC OAM recovery.
                ''',
                'catmpvclendccstatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to Up
                for the first time in the last corresponding notification 
                due to End CC OAM recovery.
                ''',
                'catmpvclendccstatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusUpTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Down to UP state transitions that has 
                happened on this PVCL in the last notification 
                interval due to End CC OAM recovery.
                ''',
                'catmpvclendccstatusuptransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclPrevFailTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to DOWN
                last time in the previous corresponding notification .
                ''',
                'catmpvclprevfailtime',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRecoveryReason', REFERENCE_ENUM_CLASS, 'CatmoamrecoverytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmoamrecoverytypeEnum', 
                [], [], 
                '''                Type of OAM Recovered
                ''',
                'catmpvclrecoveryreason',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification due to Segment CC 
                OAM recovery.
                ''',
                'catmpvclsegccstatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to Up for 
                the first time in the last corresponding notification due
                to Segment CC OAM recovery.
                ''',
                'catmpvclsegccstatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusUpTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Down to Up state transitions that has 
                happened on this PVCL in the last corresponding notification 
                due to Segment CC OAM recovery.
                ''',
                'catmpvclsegccstatusuptransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to UP 
                for the last time due to OAM loopback recovery
                in the last corresponding notification .
                ''',
                'catmpvclstatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which this PVCL changed state to UP 
                for the first time due to OAM loopback recovery
                in the last corresponding notification .
                ''',
                'catmpvclstatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusUpTransition', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of Down to Up state transitions due to
                OAM loopback recovery that has happened on this PVCL 
                in the last corresponding notification .
                ''',
                'catmpvclstatusuptransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmCurStatusUpPVclEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable',
            False, 
            [
            _MetaInfoClassMember('catmCurStatusUpPVclEntry', REFERENCE_LIST, 'Catmcurstatusuppvclentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry', 
                [], [], 
                '''                Each entry in the table represents a VCL for which
                there is an active row in the atmVclTable having an
                atmVclConnKind value of `pvc' and atmVclOperStatus
                to have changed to UP in the last PVC notification 
                interval.
                ''',
                'catmcurstatusuppvclentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmCurStatusUpPVclTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclRangeStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last Loopback OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclrangestatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first Loopback OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclrangestatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclUpHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                Loopback OAM recovery has been detected in the last 
                corresponding notification .
                ''',
                'catmpvcluphigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclUpLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                Loopback OAM recovery has been detected in the last 
                corresponding notification .
                ''',
                'catmpvcluplowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmStatusUpPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmStatusUpPVclRangeEntry', REFERENCE_LIST, 'Catmstatusuppvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and 
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and  loopback OAM status to 
                have detected as recovered in the last notification 
                interval.
                ''',
                'catmstatusuppvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmStatusUpPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclSegCCRangeStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last Segment CC OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclsegccrangestatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCRangeStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first Segment CC OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclsegccrangestatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCUpHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the
                Segment CC OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclsegccuphigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCUpLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the
                Segment CC OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclsegccuplowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmSegCCStatusUpPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmSegCCStatusUpPVclRangeEntry', REFERENCE_LIST, 'Catmsegccstatusuppvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and Segment CC OAM status to
                have detected as recovered in the last notification
                interval.
                ''',
                'catmsegccstatusuppvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmSegCCStatusUpPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclEndCCRangeStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last End-to-End CC OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclendccrangestatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCRangeStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first End-to-End CC OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclendccrangestatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCUpHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the
                End-to-End CC OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclendccuphigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCUpLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the
                End-to-End CC OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclendccuplowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmEndCCStatusUpPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmEndCCStatusUpPVclRangeEntry', REFERENCE_LIST, 'Catmendccstatusuppvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and End-to-End CC OAM status 
                to have detected as recovered in the last notification
                interval.
                ''',
                'catmendccstatusuppvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmEndCCStatusUpPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclAISRDIRangeStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last AISRDI OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclaisrdirangestatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIRangeStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first AISRDI OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclaisrdirangestatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIUpHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the
                AISRDI OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclaisrdiuphigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIUpLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the
                AISRDI OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclaisrdiuplowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmAISRDIStatusUpPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmAISRDIStatusUpPVclRangeEntry', REFERENCE_LIST, 'Catmaisrdistatusuppvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and AISRDI OAM status 
                to have detected as recovered in the last notification
                interval.
                ''',
                'catmaisrdistatusuppvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmAISRDIStatusUpPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPrevDownPVclRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last atmVclOperStatus
                is detected as Down on any of the PVCLs in the range
                in the previous catmIntfPvcDownTrap notification.
                ''',
                'catmprevdownpvclrangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPrevDownPVclRangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first atmVclOperStatus
                is detected as Down on any of the PVCLs in the range
                in the previous catmIntfPvcDownTrap notification.
                ''',
                'catmprevdownpvclrangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeRecoveryReason', REFERENCE_ENUM_CLASS, 'CatmoamrecoverytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmoamrecoverytypeEnum', 
                [], [], 
                '''                Type of OAM Recovered
                ''',
                'catmpvclrangerecoveryreason',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmVclOperStatus has been detected as Up in the 
                corresponding notification .
                ''',
                'catmuppvclhigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus has been detected as Up in the 
                corresponding notification .
                ''',
                'catmuppvcllowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the last atmVclOperStatus
                is detected as Up on any of the PVCLs in the range
                in the corresponding notification .
                ''',
                'catmuppvclrangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclRangeStart', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time stamp at which the first atmVclOperStatus
                is detected as Up on any of the PVCLs in the range
                in the corresponding notification .
                ''',
                'catmuppvclrangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmUpPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib.Catmuppvclrangetable' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib.Catmuppvclrangetable',
            False, 
            [
            _MetaInfoClassMember('catmUpPVclRangeEntry', REFERENCE_LIST, 'Catmuppvclrangeentry' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry', 
                [], [], 
                '''                Each entry in this table represents a range of VCLs and 
                for each VCL there is an active row in the atmVclTable having
                an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
                have detected as Up in the last notification 
                interval.
                ''',
                'catmuppvclrangeentry',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmUpPVclRangeTable',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CiscoAtmPvctrapExtnMib' : {
        'meta_info' : _MetaInfoClass('CiscoAtmPvctrapExtnMib',
            False, 
            [
            _MetaInfoClassMember('catmAISRDIStatusChPVclRangeTable', REFERENCE_CLASS, 'Catmaisrdistatuschpvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have changed due to AIS/RDI failure
                in the same direction in the last corresponding PVC 
                notification.
                ''',
                'catmaisrdistatuschpvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmAISRDIStatusUpPVclRangeTable', REFERENCE_CLASS, 'Catmaisrdistatusuppvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive
                range and for each VCL there is an active row in the
                atmVclTable having an atmVclConnKind value of `pvc'
                and AISRDI OAM status to have detected as recovered
                in the last corresponding PVC notification .
                ''',
                'catmaisrdistatusuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmCurStatChangePVclTable', REFERENCE_CLASS, 'Catmcurstatchangepvcltable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable', 
                [], [], 
                '''                A table indicating all VCLs for which there is an
                active row in the atmVclTable having an atmVclConnKind
                value of `pvc' and atmVclOperStatus to have changed in the
                last corresponding PVC notification.
                ''',
                'catmcurstatchangepvcltable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmCurStatusUpPVclTable', REFERENCE_CLASS, 'Catmcurstatusuppvcltable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable', 
                [], [], 
                '''                A table indicating all VCLs for which there is an
                active row in the atmVclTable having an atmVclConnKind
                value of `pvc' and atmVclOperStatus to have changed to UP
                in the last corresponding PVC notification .
                ''',
                'catmcurstatusuppvcltable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmDownPVclRangeTable', REFERENCE_CLASS, 'Catmdownpvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have detected as Down
                in the last corresponding PVC notification .
                ''',
                'catmdownpvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmEndCCStatusChPVclRangeTable', REFERENCE_CLASS, 'Catmendccstatuschpvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have changed due to End CC failure
                in the same direction in the last PVC notification 
                interval.
                ''',
                'catmendccstatuschpvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmEndCCStatusUpPVclRangeTable', REFERENCE_CLASS, 'Catmendccstatusuppvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive
                range and for each VCL there is an active row in the
                atmVclTable having an atmVclConnKind value of `pvc'
                and End-to-End CC OAM status to have detected as recovered
                in the last corresponding PVC notification .
                ''',
                'catmendccstatusuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmSegCCStatusChPVclRangeTable', REFERENCE_CLASS, 'Catmsegccstatuschpvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have changed due to segment CC 
                failure in the same direction in the last PVC 
                corresponding notification .
                ''',
                'catmsegccstatuschpvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmSegCCStatusUpPVclRangeTable', REFERENCE_CLASS, 'Catmsegccstatusuppvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive
                range and for each VCL there is an active row in the
                atmVclTable having an atmVclConnKind value of `pvc'
                and Segment CC OAM status to have detected as recovered
                in the last corresponding PVC notification .
                ''',
                'catmsegccstatusuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmStatusChangePVclRangeTable', REFERENCE_CLASS, 'Catmstatuschangepvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have changed in the same
                direction in the last corresponding PVC notification .
                ''',
                'catmstatuschangepvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmStatusUpPVclRangeTable', REFERENCE_CLASS, 'Catmstatusuppvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and loopback OAM status to have detected as recovered
                in the last corresponding PVC notification .
                ''',
                'catmstatusuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclRangeTable', REFERENCE_CLASS, 'Catmuppvclrangetable' , 'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CiscoAtmPvctrapExtnMib.Catmuppvclrangetable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have detected as Up
                in the last corresponding PVC notification .
                ''',
                'catmuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
}
_meta_table['CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable.Catmdownpvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmuppvclrangetable.Catmuppvclrangeentry']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib.Catmuppvclrangetable']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmcurstatchangepvcltable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmstatuschangepvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmsegccstatuschpvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmendccstatuschpvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmaisrdistatuschpvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmdownpvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmcurstatusuppvcltable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmstatusuppvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmsegccstatusuppvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmendccstatusuppvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmaisrdistatusuppvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
_meta_table['CiscoAtmPvctrapExtnMib.Catmuppvclrangetable']['meta_info'].parent =_meta_table['CiscoAtmPvctrapExtnMib']['meta_info']
