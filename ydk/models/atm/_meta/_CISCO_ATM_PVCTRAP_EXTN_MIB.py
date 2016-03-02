


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CatmOAMRecoveryType_Enum' : _MetaInfoEnum('CatmOAMRecoveryType_Enum', 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB',
        {
            'catmLoopbackOAMRecover':'CATMLOOPBACKOAMRECOVER',
            'catmSegmentCCOAMRecover':'CATMSEGMENTCCOAMRECOVER',
            'catmEndCCOAMRecover':'CATMENDCCOAMRECOVER',
            'catmAISRDIOAMRecover':'CATMAISRDIOAMRECOVER',
        }, 'CISCO-ATM-PVCTRAP-EXTN-MIB', _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB']),
    'CatmOAMFailureType_Enum' : _MetaInfoEnum('CatmOAMFailureType_Enum', 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB',
        {
            'catmLoopbackOAMFailure':'CATMLOOPBACKOAMFAILURE',
            'catmSegmentCCOAMFailure':'CATMSEGMENTCCOAMFAILURE',
            'catmEndCCOAMFailure':'CATMENDCCOAMFAILURE',
            'catmAISRDIOAMFailure':'CATMAISRDIOAMFAILURE',
        }, 'CISCO-ATM-PVCTRAP-EXTN-MIB', _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB']),
    'CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclAISRDIHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmOperStatus to have changed in the last 
                corresponding notification due to AISRDI OAM failure.
                ''',
                'catmpvclaisrdihigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDILowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus to have changed in the last 
                corresponding notification due to AISRDI OAM failure.
                ''',
                'catmpvclaisrdilowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIRangeStatusChEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last corresponding notification due 
                to AISRDI OAM failure.
                ''',
                'catmpvclaisrdirangestatuschend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIRangeStatusChStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmAISRDIStatusChPVclRangeEntry', REFERENCE_LIST, 'CatmAISRDIStatusChPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclAISRDIRangeStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last AISRDI OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclaisrdirangestatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIRangeStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the first AISRDI OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclaisrdirangestatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIUpHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the
                AISRDI OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclaisrdiuphigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIUpLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmAISRDIStatusUpPVclRangeEntry', REFERENCE_LIST, 'CatmAISRDIStatusUpPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclAISRDIStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification due
                to AIS RDI OAM failure.
                ''',
                'catmpvclaisrdistatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last corresponding notification due
                to AIS RDI OAM failure.
                ''',
                'catmpvclaisrdistatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last corresponding notification due
                to AIS RDI OAM failure.
                ''',
                'catmpvclaisrdistatustransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclCurFailTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to DOWN
                last time in the last corresponding notification .
                ''',
                'catmpvclcurfailtime',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification due
                to End CC OAM failure.
                ''',
                'catmpvclendccstatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last corresponding notification due
                to End CC OAM failure.
                ''',
                'catmpvclendccstatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last corresponding notification due
                to End CC OAM failure.
                ''',
                'catmpvclendccstatustransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclFailureReason', REFERENCE_ENUM_CLASS, 'CatmOAMFailureType_Enum' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMFailureType_Enum', 
                [], [], 
                '''                Type of OAM failure.
                ''',
                'catmpvclfailurereason',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclPrevRecoverTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to UP
                last time in the previous corresponding notification .
                ''',
                'catmpvclprevrecovertime',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification due
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccstatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last corresponding notification due
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccstatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last corresponding notification due
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccstatustransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification.
                ''',
                'catmpvclstatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state for the
                first time in  the last corresponding notification.
                ''',
                'catmpvclstatuschangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusTransition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of state transitions that has happened 
                on this PVCL in the last corresponding notification.
                ''',
                'catmpvclstatustransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmCurStatChangePVclEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable',
            False, 
            [
            _MetaInfoClassMember('catmCurStatChangePVclEntry', REFERENCE_LIST, 'CatmCurStatChangePVclEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclAISRDIStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to Up
                for the last time in the last corresponding notification 
                due to AIS/RDI OAM recovery.
                ''',
                'catmpvclaisrdistatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to Up
                for the first time in the last corresponding notification 
                due to AIS/RDI OAM recovery.
                ''',
                'catmpvclaisrdistatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclAISRDIStatusUpTransition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Down to Up state transitions that 
                has happened on this PVCL in the last notification 
                interval due to AIS RDI OAM recovery.
                ''',
                'catmpvclaisrdistatusuptransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclCurRecoverTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to UP
                last time in the last corresponding notification .
                ''',
                'catmpvclcurrecovertime',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to Up
                for the last time in the last corresponding notification 
                due to End CC OAM recovery.
                ''',
                'catmpvclendccstatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to Up
                for the first time in the last corresponding notification 
                due to End CC OAM recovery.
                ''',
                'catmpvclendccstatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCStatusUpTransition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Down to UP state transitions that has 
                happened on this PVCL in the last notification 
                interval due to End CC OAM recovery.
                ''',
                'catmpvclendccstatusuptransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclPrevFailTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to DOWN
                last time in the previous corresponding notification .
                ''',
                'catmpvclprevfailtime',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRecoveryReason', REFERENCE_ENUM_CLASS, 'CatmOAMRecoveryType_Enum' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMRecoveryType_Enum', 
                [], [], 
                '''                Type of OAM Recovered
                ''',
                'catmpvclrecoveryreason',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp of the last state change of this PVCL
                in the last corresponding notification due to Segment CC 
                OAM recovery.
                ''',
                'catmpvclsegccstatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to Up for 
                the first time in the last corresponding notification due
                to Segment CC OAM recovery.
                ''',
                'catmpvclsegccstatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCStatusUpTransition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Down to Up state transitions that has 
                happened on this PVCL in the last corresponding notification 
                due to Segment CC OAM recovery.
                ''',
                'catmpvclsegccstatusuptransition',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to UP 
                for the last time due to OAM loopback recovery
                in the last corresponding notification .
                ''',
                'catmpvclstatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which this PVCL changed state to UP 
                for the first time due to OAM loopback recovery
                in the last corresponding notification .
                ''',
                'catmpvclstatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclStatusUpTransition', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable',
            False, 
            [
            _MetaInfoClassMember('catmCurStatusUpPVclEntry', REFERENCE_LIST, 'CatmCurStatusUpPVclEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmDownPVclHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmVclOperStatus has been detected as Down in the 
                corresponding notification .
                ''',
                'catmdownpvclhigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmDownPVclLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus has been detected as Down in the 
                corresponding notification .
                ''',
                'catmdownpvcllowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmDownPVclRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last atmVclOperStatus
                is detected as Down on any of the PVCLs in the range
                in the corresponding notification .
                ''',
                'catmdownpvclrangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmDownPVclRangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the first atmVclOperStatus
                is detected as Down on any of the PVCLs in the range
                in the corresponding notification .
                ''',
                'catmdownpvclrangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPrevUpPVclRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last atmVclOperStatus
                is detected as Up on any of the PVCLs in the range
                in the previous catmIntfPvcUp2Trap notification.
                ''',
                'catmprevuppvclrangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPrevUpPVclRangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the first atmVclOperStatus
                is detected as Up on any of the PVCLs in the range
                in the previous catmIntfPvcUp2Trap notification.
                ''',
                'catmprevuppvclrangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeFailureReason', REFERENCE_ENUM_CLASS, 'CatmOAMFailureType_Enum' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMFailureType_Enum', 
                [], [], 
                '''                Type of OAM failure.
                ''',
                'catmpvclrangefailurereason',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            ],
            'CISCO-ATM-PVCTRAP-EXTN-MIB',
            'catmDownPVclRangeEntry',
            _yang_ns._namespaces['CISCO-ATM-PVCTRAP-EXTN-MIB'],
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmDownPVclRangeEntry', REFERENCE_LIST, 'CatmDownPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclEndCCHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmOperStatus to have changed in the last 
                corresponding notification due to End CC OAM failure.
                ''',
                'catmpvclendcchigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus to have changed in the last 
                corresponding notification due to End CC OAM failure.
                ''',
                'catmpvclendcclowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCRangeStatusChEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last corresponding notification due 
                to End CC OAM failure.
                ''',
                'catmpvclendccrangestatuschend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCRangeStatusChStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmEndCCStatusChPVclRangeEntry', REFERENCE_LIST, 'CatmEndCCStatusChPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclEndCCRangeStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last End-to-End CC OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclendccrangestatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCRangeStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the first End-to-End CC OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclendccrangestatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCUpHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the
                End-to-End CC OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclendccuphigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclEndCCUpLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmEndCCStatusUpPVclRangeEntry', REFERENCE_LIST, 'CatmEndCCStatusUpPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclSegCCHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmOperStatus to have changed in the last 
                corresponding notification due to Segment CC OAM failure.
                ''',
                'catmpvclsegcchigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus to have changed in the last 
                corresponding notification due to Segment CC OAM failure.
                ''',
                'catmpvclsegcclowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCRangeStatusChEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last corresponding notification due 
                to Segment CC OAM failure.
                ''',
                'catmpvclsegccrangestatuschend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCRangeStatusChStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmSegCCStatusChPVclRangeEntry', REFERENCE_LIST, 'CatmSegCCStatusChPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclSegCCRangeStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last Segment CC OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclsegccrangestatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCRangeStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the first Segment CC OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclsegccrangestatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCUpHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the
                Segment CC OAM recovery has been detected in the last
                corresponding notification .
                ''',
                'catmpvclsegccuphigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclSegCCUpLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmSegCCStatusUpPVclRangeEntry', REFERENCE_LIST, 'CatmSegCCStatusUpPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Index to represent different ranges, the first range is
                indexed by value 0, the second by 1 and so on...
                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmOperStatus to have changed in the last 
                corresponding notification due to Loopback OAM failure.
                ''',
                'catmpvclhigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus to have changed in the last 
                corresponding notification due to Loopback OAM failure.
                ''',
                'catmpvcllowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeStatusChangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last PVCL in the range
                changed state in the last corresponding notification due 
                to Loopback OAM failure.
                ''',
                'catmpvclrangestatuschangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeStatusChangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmStatusChangePVclRangeEntry', REFERENCE_LIST, 'CatmStatusChangePVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPVclRangeStatusUpEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last Loopback OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclrangestatusupend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeStatusUpStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the first Loopback OAM recovery
                is detected on any of the PVCLs in the range
                in the last corresponding notification .
                ''',
                'catmpvclrangestatusupstart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclUpHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                Loopback OAM recovery has been detected in the last 
                corresponding notification .
                ''',
                'catmpvcluphigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclUpLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmStatusUpPVclRangeEntry', REFERENCE_LIST, 'CatmStatusUpPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmStatusChangePVclRangeIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'catmstatuschangepvclrangeindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', True),
            _MetaInfoClassMember('catmPrevDownPVclRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last atmVclOperStatus
                is detected as Down on any of the PVCLs in the range
                in the previous catmIntfPvcDownTrap notification.
                ''',
                'catmprevdownpvclrangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPrevDownPVclRangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the first atmVclOperStatus
                is detected as Down on any of the PVCLs in the range
                in the previous catmIntfPvcDownTrap notification.
                ''',
                'catmprevdownpvclrangestart',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmPVclRangeRecoveryReason', REFERENCE_ENUM_CLASS, 'CatmOAMRecoveryType_Enum' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CatmOAMRecoveryType_Enum', 
                [], [], 
                '''                Type of OAM Recovered
                ''',
                'catmpvclrangerecoveryreason',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclHigherRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The last PVCL in a range of PVCLs for which the 
                atmVclOperStatus has been detected as Up in the 
                corresponding notification .
                ''',
                'catmuppvclhigherrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclLowerRangeValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 65536)], [], 
                '''                The first PVCL in a range of PVCLs for which the 
                atmVclOperStatus has been detected as Up in the 
                corresponding notification .
                ''',
                'catmuppvcllowerrangevalue',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclRangeEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time stamp at which the last atmVclOperStatus
                is detected as Up on any of the PVCLs in the range
                in the corresponding notification .
                ''',
                'catmuppvclrangeend',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclRangeStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable',
            False, 
            [
            _MetaInfoClassMember('catmUpPVclRangeEntry', REFERENCE_LIST, 'CatmUpPVclRangeEntry' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
    'CISCOATMPVCTRAPEXTNMIB' : {
        'meta_info' : _MetaInfoClass('CISCOATMPVCTRAPEXTNMIB',
            False, 
            [
            _MetaInfoClassMember('catmAISRDIStatusChPVclRangeTable', REFERENCE_CLASS, 'CatmAISRDIStatusChPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable', 
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
            _MetaInfoClassMember('catmAISRDIStatusUpPVclRangeTable', REFERENCE_CLASS, 'CatmAISRDIStatusUpPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive
                range and for each VCL there is an active row in the
                atmVclTable having an atmVclConnKind value of `pvc'
                and AISRDI OAM status to have detected as recovered
                in the last corresponding PVC notification .
                ''',
                'catmaisrdistatusuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmCurStatChangePVclTable', REFERENCE_CLASS, 'CatmCurStatChangePVclTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable', 
                [], [], 
                '''                A table indicating all VCLs for which there is an
                active row in the atmVclTable having an atmVclConnKind
                value of `pvc' and atmVclOperStatus to have changed in the
                last corresponding PVC notification.
                ''',
                'catmcurstatchangepvcltable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmCurStatusUpPVclTable', REFERENCE_CLASS, 'CatmCurStatusUpPVclTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable', 
                [], [], 
                '''                A table indicating all VCLs for which there is an
                active row in the atmVclTable having an atmVclConnKind
                value of `pvc' and atmVclOperStatus to have changed to UP
                in the last corresponding PVC notification .
                ''',
                'catmcurstatusuppvcltable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmDownPVclRangeTable', REFERENCE_CLASS, 'CatmDownPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have detected as Down
                in the last corresponding PVC notification .
                ''',
                'catmdownpvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmEndCCStatusChPVclRangeTable', REFERENCE_CLASS, 'CatmEndCCStatusChPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable', 
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
            _MetaInfoClassMember('catmEndCCStatusUpPVclRangeTable', REFERENCE_CLASS, 'CatmEndCCStatusUpPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive
                range and for each VCL there is an active row in the
                atmVclTable having an atmVclConnKind value of `pvc'
                and End-to-End CC OAM status to have detected as recovered
                in the last corresponding PVC notification .
                ''',
                'catmendccstatusuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmSegCCStatusChPVclRangeTable', REFERENCE_CLASS, 'CatmSegCCStatusChPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable', 
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
            _MetaInfoClassMember('catmSegCCStatusUpPVclRangeTable', REFERENCE_CLASS, 'CatmSegCCStatusUpPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive
                range and for each VCL there is an active row in the
                atmVclTable having an atmVclConnKind value of `pvc'
                and Segment CC OAM status to have detected as recovered
                in the last corresponding PVC notification .
                ''',
                'catmsegccstatusuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmStatusChangePVclRangeTable', REFERENCE_CLASS, 'CatmStatusChangePVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and atmVclOperStatus to have changed in the same
                direction in the last corresponding PVC notification .
                ''',
                'catmstatuschangepvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmStatusUpPVclRangeTable', REFERENCE_CLASS, 'CatmStatusUpPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable', 
                [], [], 
                '''                A table indicating more than one VCLs in a consecutive 
                range and for each VCL there is an active row in the 
                atmVclTable having an atmVclConnKind value of `pvc'
                and loopback OAM status to have detected as recovered
                in the last corresponding PVC notification .
                ''',
                'catmstatusuppvclrangetable',
                'CISCO-ATM-PVCTRAP-EXTN-MIB', False),
            _MetaInfoClassMember('catmUpPVclRangeTable', REFERENCE_CLASS, 'CatmUpPVclRangeTable' , 'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB', 'CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable', 
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
        'ydk.models.atm.CISCO_ATM_PVCTRAP_EXTN_MIB'
        ),
    },
}
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable.CatmAISRDIStatusChPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable.CatmAISRDIStatusUpPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable.CatmCurStatChangePVclEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable.CatmCurStatusUpPVclEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable.CatmDownPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable.CatmEndCCStatusChPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable.CatmEndCCStatusUpPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable.CatmSegCCStatusChPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable.CatmSegCCStatusUpPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable.CatmStatusChangePVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable.CatmStatusUpPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable.CatmUpPVclRangeEntry']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusChPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmAISRDIStatusUpPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatChangePVclTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmCurStatusUpPVclTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmDownPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusChPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmEndCCStatusUpPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusChPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmSegCCStatusUpPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusChangePVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmStatusUpPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
_meta_table['CISCOATMPVCTRAPEXTNMIB.CatmUpPVclRangeTable']['meta_info'].parent =_meta_table['CISCOATMPVCTRAPEXTNMIB']['meta_info']
