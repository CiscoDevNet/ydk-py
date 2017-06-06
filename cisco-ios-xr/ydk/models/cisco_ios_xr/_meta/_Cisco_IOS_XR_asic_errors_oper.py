


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData',
            False, 
            [
            _MetaInfoClassMember('crc-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                crc err count
                ''',
                'crc_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('err-count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                err count
                ''',
                'err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('gen-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                gen err count
                ''',
                'gen_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('mbe-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mbe err count
                ''',
                'mbe_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                node key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('num-nodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num nodes
                ''',
                'num_nodes',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('par-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                par err count
                ''',
                'par_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('pcie-err-count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pcie err count
                ''',
                'pcie_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('reset-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                reset err count
                ''',
                'reset_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('sbe-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sbe err count
                ''',
                'sbe_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'sum-data',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary',
            False, 
            [
            _MetaInfoClassMember('cih-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                cih client
                ''',
                'cih_client',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('legacy-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                legacy client
                ''',
                'legacy_client',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('sum-data', REFERENCE_LIST, 'SumData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData', 
                [], [], 
                '''                sum data
                ''',
                'sum_data',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath',
            False, 
            [
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary', 
                [], [], 
                '''                Summary of all instances errors
                ''',
                'summary',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'all-error-path',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.AllInstances' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.AllInstances',
            False, 
            [
            _MetaInfoClassMember('all-error-path', REFERENCE_CLASS, 'AllErrorPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath', 
                [], [], 
                '''                Error path of all instances
                ''',
                'all_error_path',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'all-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'multiple-bit-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-generic-soft',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'crc-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-sbe-soft',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'hardware-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-crc-soft',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-parity-soft',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'io-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'reset-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'barrier-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'ucode-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-reset-hard',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'single-bit-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'indirect-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'outof-resource-soft',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'crc-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'time-out-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'barrier-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-mbe-soft',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'back-pressure-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'single-bit-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'indirect-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'generic-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'link-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'configuration-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData',
            False, 
            [
            _MetaInfoClassMember('crc-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                crc err count
                ''',
                'crc_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('err-count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                err count
                ''',
                'err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('gen-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                gen err count
                ''',
                'gen_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('mbe-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mbe err count
                ''',
                'mbe_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                node key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('num-nodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num nodes
                ''',
                'num_nodes',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('par-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                par err count
                ''',
                'par_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('pcie-err-count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pcie err count
                ''',
                'pcie_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('reset-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                reset err count
                ''',
                'reset_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('sbe-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sbe err count
                ''',
                'sbe_err_count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'sum-data',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary',
            False, 
            [
            _MetaInfoClassMember('cih-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                cih client
                ''',
                'cih_client',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('legacy-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                legacy client
                ''',
                'legacy_client',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('sum-data', REFERENCE_LIST, 'SumData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData', 
                [], [], 
                '''                sum data
                ''',
                'sum_data',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'instance-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'unexpected-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'time-out-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-generic-hard',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'parity-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'descriptor-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'interface-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-sbe-hard',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-crc-hard',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-parity-hard',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-reset-soft',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'back-pressure-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'generic-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'link-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'configuration-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'multiple-bit-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'unexpected-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'outof-resource-hard',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'hardware-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'parity-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'descriptor-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'interface-soft-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'io-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'reset-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'ucode-hard-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.CsrsInfo' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.CsrsInfo',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                width
                ''',
                'width',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'csrs-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.LastErr' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.LastErr',
            False, 
            [
            _MetaInfoClassMember('at-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time
                ''',
                'at_time',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('at-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                at time nsec
                ''',
                'at_time_nsec',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('counter-val', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                counter val
                ''',
                'counter_val',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-desc', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                error desc
                ''',
                'error_desc',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('error-regval', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                error regval
                ''',
                'error_regval',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'last-err',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error',
            False, 
            [
            _MetaInfoClassMember('alarm-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                High threshold crossed
                ''',
                'alarm_on',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of rack/board/asic
                ''',
                'asic_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated count
                ''',
                'count',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('csrs-info', REFERENCE_LIST, 'CsrsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.CsrsInfo', 
                [], [], 
                '''                List of csrs_info
                ''',
                'csrs_info',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('intr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of error
                ''',
                'intr_type',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time  cleared
                ''',
                'last_cleared',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('last-err', REFERENCE_LIST, 'LastErr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.LastErr', 
                [], [], 
                '''                Last Printable error information
                ''',
                'last_err',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('leaf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Leaf ID defined in user data
                ''',
                'leaf_id',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name assigned to mem
                ''',
                'name',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                32 bit key
                ''',
                'node_key',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('period-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High period value
                ''',
                'period_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_hi',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('thresh-lo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High threshold value
                ''',
                'thresh_lo',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_LIST, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error', 
                [], [], 
                '''                Collection of errors
                ''',
                'error',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-error-mbe-hard',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath',
            False, 
            [
            _MetaInfoClassMember('asic-error-crc-hard', REFERENCE_CLASS, 'AsicErrorCrcHard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_crc_hard',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-crc-soft', REFERENCE_CLASS, 'AsicErrorCrcSoft' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_crc_soft',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-generic-hard', REFERENCE_CLASS, 'AsicErrorGenericHard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_generic_hard',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-generic-soft', REFERENCE_CLASS, 'AsicErrorGenericSoft' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_generic_soft',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-mbe-hard', REFERENCE_CLASS, 'AsicErrorMbeHard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_mbe_hard',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-mbe-soft', REFERENCE_CLASS, 'AsicErrorMbeSoft' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_mbe_soft',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-parity-hard', REFERENCE_CLASS, 'AsicErrorParityHard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_parity_hard',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-parity-soft', REFERENCE_CLASS, 'AsicErrorParitySoft' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_parity_soft',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-reset-hard', REFERENCE_CLASS, 'AsicErrorResetHard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_reset_hard',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-reset-soft', REFERENCE_CLASS, 'AsicErrorResetSoft' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_reset_soft',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-sbe-hard', REFERENCE_CLASS, 'AsicErrorSbeHard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_sbe_hard',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('asic-error-sbe-soft', REFERENCE_CLASS, 'AsicErrorSbeSoft' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'asic_error_sbe_soft',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('back-pressure-hard-errors', REFERENCE_CLASS, 'BackPressureHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors', 
                [], [], 
                '''                BP hard error information
                ''',
                'back_pressure_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('back-pressure-soft-errors', REFERENCE_CLASS, 'BackPressureSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors', 
                [], [], 
                '''                BP soft error information
                ''',
                'back_pressure_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('barrier-hard-errors', REFERENCE_CLASS, 'BarrierHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors', 
                [], [], 
                '''                Barrier hard error information
                ''',
                'barrier_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('barrier-soft-errors', REFERENCE_CLASS, 'BarrierSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors', 
                [], [], 
                '''                Barrier soft error information
                ''',
                'barrier_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('configuration-hard-errors', REFERENCE_CLASS, 'ConfigurationHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors', 
                [], [], 
                '''                Configuration hard error information
                ''',
                'configuration_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('configuration-soft-errors', REFERENCE_CLASS, 'ConfigurationSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors', 
                [], [], 
                '''                Configuration soft error information
                ''',
                'configuration_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('crc-hard-errors', REFERENCE_CLASS, 'CrcHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors', 
                [], [], 
                '''                CRC hard error information
                ''',
                'crc_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('crc-soft-errors', REFERENCE_CLASS, 'CrcSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors', 
                [], [], 
                '''                CRC soft error information
                ''',
                'crc_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('descriptor-hard-errors', REFERENCE_CLASS, 'DescriptorHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors', 
                [], [], 
                '''                Descriptor hard error information
                ''',
                'descriptor_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('descriptor-soft-errors', REFERENCE_CLASS, 'DescriptorSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors', 
                [], [], 
                '''                Descriptor soft error information
                ''',
                'descriptor_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('generic-hard-errors', REFERENCE_CLASS, 'GenericHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors', 
                [], [], 
                '''                Generic hard error information
                ''',
                'generic_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('generic-soft-errors', REFERENCE_CLASS, 'GenericSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors', 
                [], [], 
                '''                Generic soft error information
                ''',
                'generic_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('hardware-hard-errors', REFERENCE_CLASS, 'HardwareHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors', 
                [], [], 
                '''                Hardware hard error information
                ''',
                'hardware_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('hardware-soft-errors', REFERENCE_CLASS, 'HardwareSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors', 
                [], [], 
                '''                Hardware soft error information
                ''',
                'hardware_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('indirect-hard-errors', REFERENCE_CLASS, 'IndirectHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors', 
                [], [], 
                '''                Indirect hard error information
                ''',
                'indirect_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('indirect-soft-errors', REFERENCE_CLASS, 'IndirectSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors', 
                [], [], 
                '''                Indirect soft error information
                ''',
                'indirect_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('instance-summary', REFERENCE_CLASS, 'InstanceSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary', 
                [], [], 
                '''                Summary for a specific instance
                ''',
                'instance_summary',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('interface-hard-errors', REFERENCE_CLASS, 'InterfaceHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors', 
                [], [], 
                '''                Interface hard error information
                ''',
                'interface_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('interface-soft-errors', REFERENCE_CLASS, 'InterfaceSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors', 
                [], [], 
                '''                Interface soft error information
                ''',
                'interface_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('io-hard-errors', REFERENCE_CLASS, 'IoHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors', 
                [], [], 
                '''                IO hard error information
                ''',
                'io_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('io-soft-errors', REFERENCE_CLASS, 'IoSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors', 
                [], [], 
                '''                IO soft error information
                ''',
                'io_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('link-hard-errors', REFERENCE_CLASS, 'LinkHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors', 
                [], [], 
                '''                Link hard error information
                ''',
                'link_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('link-soft-errors', REFERENCE_CLASS, 'LinkSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors', 
                [], [], 
                '''                Link soft error information
                ''',
                'link_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('multiple-bit-hard-errors', REFERENCE_CLASS, 'MultipleBitHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors', 
                [], [], 
                '''                Multiple bit hard error information
                ''',
                'multiple_bit_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('multiple-bit-soft-errors', REFERENCE_CLASS, 'MultipleBitSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors', 
                [], [], 
                '''                Multiple bit soft error information
                ''',
                'multiple_bit_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('outof-resource-hard', REFERENCE_CLASS, 'OutofResourceHard' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard', 
                [], [], 
                '''                OOR thresh information
                ''',
                'outof_resource_hard',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('outof-resource-soft', REFERENCE_CLASS, 'OutofResourceSoft' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft', 
                [], [], 
                '''                OOR thresh information
                ''',
                'outof_resource_soft',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('parity-hard-errors', REFERENCE_CLASS, 'ParityHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors', 
                [], [], 
                '''                Parity hard error information
                ''',
                'parity_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('parity-soft-errors', REFERENCE_CLASS, 'ParitySoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors', 
                [], [], 
                '''                Parity soft error information
                ''',
                'parity_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('reset-hard-errors', REFERENCE_CLASS, 'ResetHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors', 
                [], [], 
                '''                Reset hard error information
                ''',
                'reset_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('reset-soft-errors', REFERENCE_CLASS, 'ResetSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors', 
                [], [], 
                '''                Reset soft error information
                ''',
                'reset_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('single-bit-hard-errors', REFERENCE_CLASS, 'SingleBitHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors', 
                [], [], 
                '''                Single bit hard error information
                ''',
                'single_bit_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('single-bit-soft-errors', REFERENCE_CLASS, 'SingleBitSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors', 
                [], [], 
                '''                Single bit soft error information
                ''',
                'single_bit_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('time-out-hard-errors', REFERENCE_CLASS, 'TimeOutHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors', 
                [], [], 
                '''                Time out hard error information
                ''',
                'time_out_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('time-out-soft-errors', REFERENCE_CLASS, 'TimeOutSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors', 
                [], [], 
                '''                Time out soft error information
                ''',
                'time_out_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('ucode-hard-errors', REFERENCE_CLASS, 'UcodeHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors', 
                [], [], 
                '''                UCode hard error information
                ''',
                'ucode_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('ucode-soft-errors', REFERENCE_CLASS, 'UcodeSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors', 
                [], [], 
                '''                Ucode soft error information
                ''',
                'ucode_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('unexpected-hard-errors', REFERENCE_CLASS, 'UnexpectedHardErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors', 
                [], [], 
                '''                Unexpected hard error information
                ''',
                'unexpected_hard_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('unexpected-soft-errors', REFERENCE_CLASS, 'UnexpectedSoftErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors', 
                [], [], 
                '''                Unexpected soft error information
                ''',
                'unexpected_soft_errors',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'error-path',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances.Instance',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-asic-errors-oper', True),
            _MetaInfoClassMember('error-path', REFERENCE_CLASS, 'ErrorPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath', 
                [], [], 
                '''                Error path of the instances
                ''',
                'error_path',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation.Instances' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation.Instances',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances.Instance', 
                [], [], 
                '''                Particular asic instance on the node
                ''',
                'instance',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'instances',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node.AsicInformation' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node.AsicInformation',
            False, 
            [
            _MetaInfoClassMember('asic', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Asic string
                ''',
                'asic',
                'Cisco-IOS-XR-asic-errors-oper', True),
            _MetaInfoClassMember('all-instances', REFERENCE_CLASS, 'AllInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.AllInstances', 
                [], [], 
                '''                All asic instance on the node
                ''',
                'all_instances',
                'Cisco-IOS-XR-asic-errors-oper', False),
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation.Instances', 
                [], [], 
                '''                All asic errors  on the node
                ''',
                'instances',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-information',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-asic-errors-oper', True),
            _MetaInfoClassMember('asic-information', REFERENCE_LIST, 'AsicInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node.AsicInformation', 
                [], [], 
                '''                Asic on the node
                ''',
                'asic_information',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors.Nodes' : {
        'meta_info' : _MetaInfoClass('AsicErrors.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes.Node', 
                [], [], 
                '''                Asic error for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
    'AsicErrors' : {
        'meta_info' : _MetaInfoClass('AsicErrors',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper', 'AsicErrors.Nodes', 
                [], [], 
                '''                Asic errors for each available nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asic-errors-oper',
            'asic-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper'
        ),
    },
}
_meta_table['AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.AllInstances']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.CsrsInfo']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.LastErr']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances.Instance']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.AllInstances']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation.Instances']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node.AsicInformation']['meta_info']
_meta_table['AsicErrors.Nodes.Node.AsicInformation']['meta_info'].parent =_meta_table['AsicErrors.Nodes.Node']['meta_info']
_meta_table['AsicErrors.Nodes.Node']['meta_info'].parent =_meta_table['AsicErrors.Nodes']['meta_info']
_meta_table['AsicErrors.Nodes']['meta_info'].parent =_meta_table['AsicErrors']['meta_info']
