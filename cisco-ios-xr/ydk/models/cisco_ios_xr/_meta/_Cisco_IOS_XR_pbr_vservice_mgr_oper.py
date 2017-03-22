


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VsNshStatsEnum' : _MetaInfoEnum('VsNshStatsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper',
        {
            'vs-nsh-stats-spi-si':'vs_nsh_stats_spi_si',
            'vs-nsh-stats-ter-min-ate':'vs_nsh_stats_ter_min_ate',
            'vs-nsh-stats-sf':'vs_nsh_stats_sf',
            'vs-nsh-stats-sff':'vs_nsh_stats_sff',
            'vs-nsh-stats-sff-local':'vs_nsh_stats_sff_local',
            'vs-nsh-stats-sfp':'vs_nsh_stats_sfp',
            'vs-nsh-stats-sfp-detail':'vs_nsh_stats_sfp_detail',
            'vs-nsh-stats-max':'vs_nsh_stats_max',
        }, 'Cisco-IOS-XR-pbr-vservice-mgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper']),
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi', 
                [], [], 
                '''                Service index counters
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term', 
                [], [], 
                '''                Terminate counters
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sf',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal',
            False, 
            [
            _MetaInfoClassMember('lookup-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with unknown spi-si
                ''',
                'lookup_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('lookup-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with unknown spi-si
                ''',
                'lookup_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with invalid NSH header
                ''',
                'malformed_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with invalid NSH header
                ''',
                'malformed_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff-local',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data',
            False, 
            [
            _MetaInfoClassMember('sf', REFERENCE_CLASS, 'Sf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf', 
                [], [], 
                '''                Service function stats
                ''',
                'sf',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff', REFERENCE_CLASS, 'Sff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff', 
                [], [], 
                '''                Service function forwarder stats
                ''',
                'sff',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff-local', REFERENCE_CLASS, 'SffLocal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal', 
                [], [], 
                '''                Local service function forwarder stats
                ''',
                'sff_local',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sfp', REFERENCE_CLASS, 'Sfp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp', 
                [], [], 
                '''                SFP stats
                ''',
                'sfp',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi', 
                [], [], 
                '''                SPI SI stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi', 
                [], [], 
                '''                SF/SFF stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data', 
                [], [], 
                '''                Stats counter for this index
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Service index
                ''',
                'si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'si-arr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data', 
                [], [], 
                '''                Statistics data
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si-arr', REFERENCE_LIST, 'SiArr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr', 
                [], [], 
                '''                SI array in case of detail stats
                ''',
                'si_arr',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi', 
                [], [], 
                '''                Service index counters
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term', 
                [], [], 
                '''                Terminate counters
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sf',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal',
            False, 
            [
            _MetaInfoClassMember('lookup-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with unknown spi-si
                ''',
                'lookup_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('lookup-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with unknown spi-si
                ''',
                'lookup_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with invalid NSH header
                ''',
                'malformed_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with invalid NSH header
                ''',
                'malformed_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff-local',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data',
            False, 
            [
            _MetaInfoClassMember('sf', REFERENCE_CLASS, 'Sf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf', 
                [], [], 
                '''                Service function stats
                ''',
                'sf',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff', REFERENCE_CLASS, 'Sff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff', 
                [], [], 
                '''                Service function forwarder stats
                ''',
                'sff',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff-local', REFERENCE_CLASS, 'SffLocal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal', 
                [], [], 
                '''                Local service function forwarder stats
                ''',
                'sff_local',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sfp', REFERENCE_CLASS, 'Sfp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp', 
                [], [], 
                '''                SFP stats
                ''',
                'sfp',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi', 
                [], [], 
                '''                SPI SI stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi', 
                [], [], 
                '''                SF/SFF stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data', 
                [], [], 
                '''                Stats counter for this index
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Service index
                ''',
                'si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'si-arr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data', 
                [], [], 
                '''                Statistics data
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si-arr', REFERENCE_LIST, 'SiArr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr', 
                [], [], 
                '''                SI array in case of detail stats
                ''',
                'si_arr',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'summarized',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats',
            False, 
            [
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail', 
                [], [], 
                '''                Detail statistics per service index 
                ''',
                'detail',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('summarized', REFERENCE_CLASS, 'Summarized' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized', 
                [], [], 
                '''                Combined statistics of all service index in
                service functionpath
                ''',
                'summarized',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi', 
                [], [], 
                '''                Service index counters
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term', 
                [], [], 
                '''                Terminate counters
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sf',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal',
            False, 
            [
            _MetaInfoClassMember('lookup-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with unknown spi-si
                ''',
                'lookup_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('lookup-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with unknown spi-si
                ''',
                'lookup_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with invalid NSH header
                ''',
                'malformed_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with invalid NSH header
                ''',
                'malformed_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff-local',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data',
            False, 
            [
            _MetaInfoClassMember('sf', REFERENCE_CLASS, 'Sf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf', 
                [], [], 
                '''                Service function stats
                ''',
                'sf',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff', REFERENCE_CLASS, 'Sff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff', 
                [], [], 
                '''                Service function forwarder stats
                ''',
                'sff',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff-local', REFERENCE_CLASS, 'SffLocal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal', 
                [], [], 
                '''                Local service function forwarder stats
                ''',
                'sff_local',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sfp', REFERENCE_CLASS, 'Sfp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp', 
                [], [], 
                '''                SFP stats
                ''',
                'sfp',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi', 
                [], [], 
                '''                SPI SI stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi', 
                [], [], 
                '''                SF/SFF stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data', 
                [], [], 
                '''                Stats counter for this index
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Service index
                ''',
                'si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'si-arr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Service Index
                ''',
                'index',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', True),
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data', 
                [], [], 
                '''                Statistics data
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si-arr', REFERENCE_LIST, 'SiArr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr', 
                [], [], 
                '''                SI array in case of detail stats
                ''',
                'si_arr',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'service-index',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes',
            False, 
            [
            _MetaInfoClassMember('service-index', REFERENCE_LIST, 'ServiceIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex', 
                [], [], 
                '''                Service index operational data belonging to
                this path
                ''',
                'service_index',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'service-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Specific Service-Function-Path identifier
                ''',
                'id',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', True),
            _MetaInfoClassMember('service-indexes', REFERENCE_CLASS, 'ServiceIndexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes', 
                [], [], 
                '''                Service Index Belonging to Path
                ''',
                'service_indexes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats', 
                [], [], 
                '''                SFP Statistics
                ''',
                'stats',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'path-id',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds',
            False, 
            [
            _MetaInfoClassMember('path-id', REFERENCE_LIST, 'PathId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId', 
                [], [], 
                '''                Specific Service-Function-Path identifier 
                ''',
                'path_id',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'path-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionPath' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionPath',
            False, 
            [
            _MetaInfoClassMember('path-ids', REFERENCE_CLASS, 'PathIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds', 
                [], [], 
                '''                Service Function Path Id 
                ''',
                'path_ids',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'service-function-path',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi', 
                [], [], 
                '''                Service index counters
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term', 
                [], [], 
                '''                Terminate counters
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sf',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal',
            False, 
            [
            _MetaInfoClassMember('lookup-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with unknown spi-si
                ''',
                'lookup_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('lookup-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with unknown spi-si
                ''',
                'lookup_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with invalid NSH header
                ''',
                'malformed_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with invalid NSH header
                ''',
                'malformed_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff-local',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data',
            False, 
            [
            _MetaInfoClassMember('sf', REFERENCE_CLASS, 'Sf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf', 
                [], [], 
                '''                Service function stats
                ''',
                'sf',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff', REFERENCE_CLASS, 'Sff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff', 
                [], [], 
                '''                Service function forwarder stats
                ''',
                'sff',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff-local', REFERENCE_CLASS, 'SffLocal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal', 
                [], [], 
                '''                Local service function forwarder stats
                ''',
                'sff_local',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sfp', REFERENCE_CLASS, 'Sfp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp', 
                [], [], 
                '''                SFP stats
                ''',
                'sfp',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi', 
                [], [], 
                '''                SPI SI stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi', 
                [], [], 
                '''                SF/SFF stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data', 
                [], [], 
                '''                Stats counter for this index
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Service index
                ''',
                'si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'si-arr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name
                ''',
                'name',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', True),
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data', 
                [], [], 
                '''                Statistics data
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si-arr', REFERENCE_LIST, 'SiArr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr', 
                [], [], 
                '''                SI array in case of detail stats
                ''',
                'si_arr',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sf-name',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction.SfNames' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction.SfNames',
            False, 
            [
            _MetaInfoClassMember('sf-name', REFERENCE_LIST, 'SfName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName', 
                [], [], 
                '''                Name of Service Function
                ''',
                'sf_name',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sf-names',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunction' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunction',
            False, 
            [
            _MetaInfoClassMember('sf-names', REFERENCE_CLASS, 'SfNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction.SfNames', 
                [], [], 
                '''                List of Service Function Names
                ''',
                'sf_names',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'service-function',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi', 
                [], [], 
                '''                Service index counters
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term', 
                [], [], 
                '''                Terminate counters
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sf',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal',
            False, 
            [
            _MetaInfoClassMember('lookup-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with unknown spi-si
                ''',
                'lookup_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('lookup-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with unknown spi-si
                ''',
                'lookup_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with invalid NSH header
                ''',
                'malformed_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with invalid NSH header
                ''',
                'malformed_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff-local',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data',
            False, 
            [
            _MetaInfoClassMember('sf', REFERENCE_CLASS, 'Sf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf', 
                [], [], 
                '''                Service function stats
                ''',
                'sf',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff', REFERENCE_CLASS, 'Sff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff', 
                [], [], 
                '''                Service function forwarder stats
                ''',
                'sff',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff-local', REFERENCE_CLASS, 'SffLocal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal', 
                [], [], 
                '''                Local service function forwarder stats
                ''',
                'sff_local',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sfp', REFERENCE_CLASS, 'Sfp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp', 
                [], [], 
                '''                SFP stats
                ''',
                'sfp',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi', 
                [], [], 
                '''                SPI SI stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi', 
                [], [], 
                '''                SF/SFF stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data', 
                [], [], 
                '''                Stats counter for this index
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Service index
                ''',
                'si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'si-arr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name
                ''',
                'name',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', True),
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data', 
                [], [], 
                '''                Statistics data
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si-arr', REFERENCE_LIST, 'SiArr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr', 
                [], [], 
                '''                SI array in case of detail stats
                ''',
                'si_arr',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff-name',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames',
            False, 
            [
            _MetaInfoClassMember('sff-name', REFERENCE_LIST, 'SffName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName', 
                [], [], 
                '''                Name of Service Function Forwarder
                ''',
                'sff_name',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff-names',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi', 
                [], [], 
                '''                Service index counters
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term', 
                [], [], 
                '''                Terminate counters
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sfp',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sf',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal',
            False, 
            [
            _MetaInfoClassMember('lookup-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with unknown spi-si
                ''',
                'lookup_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('lookup-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with unknown spi-si
                ''',
                'lookup_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes with invalid NSH header
                ''',
                'malformed_err_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('malformed-err-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets with invalid NSH header
                ''',
                'malformed_err_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'sff-local',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data',
            False, 
            [
            _MetaInfoClassMember('sf', REFERENCE_CLASS, 'Sf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf', 
                [], [], 
                '''                Service function stats
                ''',
                'sf',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff', REFERENCE_CLASS, 'Sff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff', 
                [], [], 
                '''                Service function forwarder stats
                ''',
                'sff',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff-local', REFERENCE_CLASS, 'SffLocal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal', 
                [], [], 
                '''                Local service function forwarder stats
                ''',
                'sff_local',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sfp', REFERENCE_CLASS, 'Sfp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp', 
                [], [], 
                '''                SFP stats
                ''',
                'sfp',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi', 
                [], [], 
                '''                SPI SI stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi',
            False, 
            [
            _MetaInfoClassMember('processed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes processed
                ''',
                'processed_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('processed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets processed
                ''',
                'processed_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'spi-si',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term',
            False, 
            [
            _MetaInfoClassMember('terminated-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes terminated
                ''',
                'terminated_bytes',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('terminated-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of terminated packets
                ''',
                'terminated_pkts',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'term',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data',
            False, 
            [
            _MetaInfoClassMember('spi-si', REFERENCE_CLASS, 'SpiSi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi', 
                [], [], 
                '''                SF/SFF stats
                ''',
                'spi_si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('term', REFERENCE_CLASS, 'Term' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term', 
                [], [], 
                '''                Terminate stats
                ''',
                'term',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'VsNshStatsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'VsNshStatsEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'data',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data', 
                [], [], 
                '''                Stats counter for this index
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Service index
                ''',
                'si',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'si-arr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error',
            False, 
            [
            _MetaInfoClassMember('data', REFERENCE_CLASS, 'Data' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data', 
                [], [], 
                '''                Statistics data
                ''',
                'data',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('si-arr', REFERENCE_LIST, 'SiArr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr', 
                [], [], 
                '''                SI array in case of detail stats
                ''',
                'si_arr',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_CLASS, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error', 
                [], [], 
                '''                Error Statistics for local service function
                forwarder
                ''',
                'error',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'local',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining.ServiceFunctionForwarder' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining.ServiceFunctionForwarder',
            False, 
            [
            _MetaInfoClassMember('local', REFERENCE_CLASS, 'Local' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local', 
                [], [], 
                '''                Local Service Function Forwarder operational
                data
                ''',
                'local',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('sff-names', REFERENCE_CLASS, 'SffNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames', 
                [], [], 
                '''                List of Service Function Forwarder Names
                ''',
                'sff_names',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'service-function-forwarder',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
    'GlobalServiceFunctionChaining' : {
        'meta_info' : _MetaInfoClass('GlobalServiceFunctionChaining',
            False, 
            [
            _MetaInfoClassMember('service-function', REFERENCE_CLASS, 'ServiceFunction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunction', 
                [], [], 
                '''                Service Function operational data
                ''',
                'service_function',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('service-function-forwarder', REFERENCE_CLASS, 'ServiceFunctionForwarder' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionForwarder', 
                [], [], 
                '''                Service Function Forwarder operational data
                ''',
                'service_function_forwarder',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            _MetaInfoClassMember('service-function-path', REFERENCE_CLASS, 'ServiceFunctionPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper', 'GlobalServiceFunctionChaining.ServiceFunctionPath', 
                [], [], 
                '''                Service Function Path operational data
                ''',
                'service_function_path',
                'Cisco-IOS-XR-pbr-vservice-mgr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-vservice-mgr-oper',
            'global-service-function-chaining',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-vservice-mgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_mgr_oper'
        ),
    },
}
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Detail']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats.Summarized']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.Stats']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId.ServiceIndexes']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds.PathId']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath.PathIds']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sfp']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sf']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.Sff']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data.SffLocal']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName.SiArr']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames.SfName']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction.SfNames']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunction']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sf']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.Sff']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName.SiArr']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames.SffName']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sfp']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sf']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.Sff']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data.SffLocal']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.Data']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error.SiArr']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local.Error']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.SffNames']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder.Local']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionPath']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunction']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining']['meta_info']
_meta_table['GlobalServiceFunctionChaining.ServiceFunctionForwarder']['meta_info'].parent =_meta_table['GlobalServiceFunctionChaining']['meta_info']
