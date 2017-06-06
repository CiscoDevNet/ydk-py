


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PmThresholdRearmEnum' : _MetaInfoEnum('PmThresholdRearmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg',
        {
            'always':'always',
            'window':'window',
            'toggle':'toggle',
        }, 'Cisco-IOS-XR-manageability-perfmgmt-cfg', _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg']),
    'PmThresholdOpEnum' : _MetaInfoEnum('PmThresholdOpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg',
        {
            'eq':'eq',
            'ne':'ne',
            'lt':'lt',
            'le':'le',
            'gt':'gt',
            'ge':'ge',
            'rg':'rg',
        }, 'Cisco-IOS-XR-manageability-perfmgmt-cfg', _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg']),
    'PerfMgmt.Resources.TftpResources' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Resources.TftpResources',
            False, 
            [
            _MetaInfoClassMember('directory', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Directory name on TFTP server
                ''',
                'directory',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the TFTP server
                ''',
                'server_address',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'tftp-resources',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Resources.DumpLocal' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Resources.DumpLocal',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable data dump onto local filesystem
                ''',
                'enable',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'dump-local',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Resources.MemoryResources' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Resources.MemoryResources',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum limit for memory usage (Kbytes) for
                data buffers
                ''',
                'max_limit',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('min-reserved', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specify a minimum free memory (Kbytes) to be
                ensured before allowing a collection request
                ''',
                'min_reserved',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'memory-resources',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Resources' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Resources',
            False, 
            [
            _MetaInfoClassMember('dump-local', REFERENCE_CLASS, 'DumpLocal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Resources.DumpLocal', 
                [], [], 
                '''                Configure local dump parameters
                ''',
                'dump_local',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('memory-resources', REFERENCE_CLASS, 'MemoryResources' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Resources.MemoryResources', 
                [], [], 
                '''                Configure the memory usage limits of
                performance management
                ''',
                'memory_resources',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('tftp-resources', REFERENCE_CLASS, 'TftpResources' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Resources.TftpResources', 
                [], [], 
                '''                Configure the TFTP server IP address and
                directory name
                ''',
                'tftp_resources',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'resources',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.GenericCounterInterface.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.GenericCounterInterface.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.GenericCounterInterface.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.GenericCounterInterface.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.GenericCounterInterface.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.GenericCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.GenericCounterInterface',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.GenericCounterInterface.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'generic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.ProcessNode.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.ProcessNode.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.ProcessNode.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.ProcessNode.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.ProcessNode.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.ProcessNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.ProcessNode',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.ProcessNode.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.BasicCounterInterface.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.BasicCounterInterface.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.BasicCounterInterface.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.BasicCounterInterface.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.BasicCounterInterface.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.BasicCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.BasicCounterInterface',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.BasicCounterInterface.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'basic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Ospfv3Protocol.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Ospfv3Protocol.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Ospfv3Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Ospfv3Protocol',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Ospfv3Protocol.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv3-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.CpuNode.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.CpuNode.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.CpuNode.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.CpuNode.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.CpuNode.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.CpuNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.CpuNode',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.CpuNode.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'cpu-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.DataRateInterface.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.DataRateInterface.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.DataRateInterface.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.DataRateInterface.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.DataRateInterface.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.DataRateInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.DataRateInterface',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.DataRateInterface.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'data-rate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.MemoryNode.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.MemoryNode.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.MemoryNode.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.MemoryNode.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.MemoryNode.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.MemoryNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.MemoryNode',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.MemoryNode.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'memory-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.LdpMpls.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.LdpMpls.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.LdpMpls.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.LdpMpls.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.LdpMpls.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.LdpMpls' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.LdpMpls',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.LdpMpls.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ldp-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Bgp.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Bgp.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Bgp.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Bgp.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Bgp.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Bgp' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Bgp',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Bgp.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('history-persistent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable persistent history statistics
                ''',
                'history_persistent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular
                expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of each sample in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Number of samples to be taken
                ''',
                'sample_size',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group configured in regular expression to
                be applied
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Ospfv2Protocol.Templates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Ospfv2Protocol.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template', 
                [], [], 
                '''                A template instance
                ''',
                'template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics.Ospfv2Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics.Ospfv2Protocol',
            False, 
            [
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Ospfv2Protocol.Templates', 
                [], [], 
                '''                Template name
                ''',
                'templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv2-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Statistics' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Statistics',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interface', REFERENCE_CLASS, 'BasicCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.BasicCounterInterface', 
                [], [], 
                '''                Interface BasicCounter collection templates
                ''',
                'basic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Bgp', 
                [], [], 
                '''                BGP collection templates
                ''',
                'bgp',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('cpu-node', REFERENCE_CLASS, 'CpuNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.CpuNode', 
                [], [], 
                '''                Node CPU collection templates
                ''',
                'cpu_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('data-rate-interface', REFERENCE_CLASS, 'DataRateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.DataRateInterface', 
                [], [], 
                '''                Interface DataRate collection templates
                ''',
                'data_rate_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('generic-counter-interface', REFERENCE_CLASS, 'GenericCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.GenericCounterInterface', 
                [], [], 
                '''                Interface Generic GenericCounter collection
                templates
                ''',
                'generic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ldp-mpls', REFERENCE_CLASS, 'LdpMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.LdpMpls', 
                [], [], 
                '''                MPLS LDP collection templates
                ''',
                'ldp_mpls',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('memory-node', REFERENCE_CLASS, 'MemoryNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.MemoryNode', 
                [], [], 
                '''                Node Memory collection templates
                ''',
                'memory_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv2-protocol', REFERENCE_CLASS, 'Ospfv2Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Ospfv2Protocol', 
                [], [], 
                '''                OSPF v2 Protocol collection templates
                ''',
                'ospfv2_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv3-protocol', REFERENCE_CLASS, 'Ospfv3Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.Ospfv3Protocol', 
                [], [], 
                '''                OSPF v3 Protocol collection templates
                ''',
                'ospfv3_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('process-node', REFERENCE_CLASS, 'ProcessNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics.ProcessNode', 
                [], [], 
                '''                Node Process collection templates
                ''',
                'process_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.Ospfv3Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.Ospfv3Protocol',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv3-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.Bgp' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.Bgp',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.DataRateInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.DataRateInterface',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'data-rate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.Ospfv2Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.Ospfv2Protocol',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv2-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.MemoryNode.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.MemoryNode.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node', 
                [], [], 
                '''                Node instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.MemoryNode.NodeAll' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.MemoryNode.NodeAll',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node-all',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.MemoryNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.MemoryNode',
            False, 
            [
            _MetaInfoClassMember('node-all', REFERENCE_CLASS, 'NodeAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.MemoryNode.NodeAll', 
                [], [], 
                '''                All the the nodes
                ''',
                'node_all',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.MemoryNode.Nodes', 
                [], [], 
                '''                Node specification
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'memory-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.GenericCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.GenericCounterInterface',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'generic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.CpuNode.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.CpuNode.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node', 
                [], [], 
                '''                Node instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.CpuNode.NodeAll' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.CpuNode.NodeAll',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node-all',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.CpuNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.CpuNode',
            False, 
            [
            _MetaInfoClassMember('node-all', REFERENCE_CLASS, 'NodeAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.CpuNode.NodeAll', 
                [], [], 
                '''                All the the nodes
                ''',
                'node_all',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.CpuNode.Nodes', 
                [], [], 
                '''                Node specification
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'cpu-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.LdpMpls' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.LdpMpls',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ldp-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.ProcessNode.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.ProcessNode.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node', 
                [], [], 
                '''                Node instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.ProcessNode.NodeAll' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.ProcessNode.NodeAll',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node-all',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.ProcessNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.ProcessNode',
            False, 
            [
            _MetaInfoClassMember('node-all', REFERENCE_CLASS, 'NodeAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.ProcessNode.NodeAll', 
                [], [], 
                '''                All the the nodes
                ''',
                'node_all',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.ProcessNode.Nodes', 
                [], [], 
                '''                Node specification
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold.BasicCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold.BasicCounterInterface',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'basic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Threshold' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Threshold',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interface', REFERENCE_CLASS, 'BasicCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.BasicCounterInterface', 
                [], [], 
                '''                Threshold monitoring for Interface
                basic-counters
                ''',
                'basic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.Bgp', 
                [], [], 
                '''                Threshold monitoring for BGP
                ''',
                'bgp',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('cpu-node', REFERENCE_CLASS, 'CpuNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.CpuNode', 
                [], [], 
                '''                Threshold monitoring for CPU
                ''',
                'cpu_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('data-rate-interface', REFERENCE_CLASS, 'DataRateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.DataRateInterface', 
                [], [], 
                '''                Threshold monitoring for Interface  data-rates
                ''',
                'data_rate_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('generic-counter-interface', REFERENCE_CLASS, 'GenericCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.GenericCounterInterface', 
                [], [], 
                '''                Threshold monitoring for Interface
                generic-counters
                ''',
                'generic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ldp-mpls', REFERENCE_CLASS, 'LdpMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.LdpMpls', 
                [], [], 
                '''                Threshold monitoring for LDP
                ''',
                'ldp_mpls',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('memory-node', REFERENCE_CLASS, 'MemoryNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.MemoryNode', 
                [], [], 
                '''                Threshold monitoring for memory
                ''',
                'memory_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv2-protocol', REFERENCE_CLASS, 'Ospfv2Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.Ospfv2Protocol', 
                [], [], 
                '''                Threshold monitoring for OSPF v2 Protocol
                ''',
                'ospfv2_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv3-protocol', REFERENCE_CLASS, 'Ospfv3Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.Ospfv3Protocol', 
                [], [], 
                '''                Threshold monitoring for OSPF v3 Protocol
                ''',
                'ospfv3_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('process-node', REFERENCE_CLASS, 'ProcessNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold.ProcessNode', 
                [], [], 
                '''                Threshold monitoring for process
                ''',
                'process_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.GenericCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.GenericCounterInterface',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'generic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.Bgp' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.Bgp',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.Ospfv2Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.Ospfv2Protocol',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv2-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.Ospfv3Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.Ospfv3Protocol',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv3-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.CpuNode.NodeAll' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.CpuNode.NodeAll',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node-all',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.CpuNode.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.CpuNode.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node', 
                [], [], 
                '''                Node instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.CpuNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.CpuNode',
            False, 
            [
            _MetaInfoClassMember('node-all', REFERENCE_CLASS, 'NodeAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.CpuNode.NodeAll', 
                [], [], 
                '''                All the the nodes
                ''',
                'node_all',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.CpuNode.Nodes', 
                [], [], 
                '''                Node specification
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'cpu-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.BasicCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.BasicCounterInterface',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'basic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.ProcessNode.NodeAll' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.ProcessNode.NodeAll',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node-all',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.ProcessNode.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.ProcessNode.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node', 
                [], [], 
                '''                Node instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.ProcessNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.ProcessNode',
            False, 
            [
            _MetaInfoClassMember('node-all', REFERENCE_CLASS, 'NodeAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.ProcessNode.NodeAll', 
                [], [], 
                '''                All the the nodes
                ''',
                'node_all',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.ProcessNode.Nodes', 
                [], [], 
                '''                Node specification
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.DataRateInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.DataRateInterface',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'data-rate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.MemoryNode.NodeAll' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.MemoryNode.NodeAll',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node-all',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.MemoryNode.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.MemoryNode.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node', 
                [], [], 
                '''                Node instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.MemoryNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.MemoryNode',
            False, 
            [
            _MetaInfoClassMember('node-all', REFERENCE_CLASS, 'NodeAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.MemoryNode.NodeAll', 
                [], [], 
                '''                All the the nodes
                ''',
                'node_all',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.MemoryNode.Nodes', 
                [], [], 
                '''                Node specification
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'memory-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics.LdpMpls' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics.LdpMpls',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ldp-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.Statistics' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.Statistics',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interface', REFERENCE_CLASS, 'BasicCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.BasicCounterInterface', 
                [], [], 
                '''                Statistics collection for basic-counters
                ''',
                'basic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.Bgp', 
                [], [], 
                '''                Data collection for BGP
                ''',
                'bgp',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('cpu-node', REFERENCE_CLASS, 'CpuNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.CpuNode', 
                [], [], 
                '''                Collection for CPU
                ''',
                'cpu_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('data-rate-interface', REFERENCE_CLASS, 'DataRateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.DataRateInterface', 
                [], [], 
                '''                Statistics collection for generic-counters
                ''',
                'data_rate_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('generic-counter-interface', REFERENCE_CLASS, 'GenericCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.GenericCounterInterface', 
                [], [], 
                '''                Statistics collection for generic-counters
                ''',
                'generic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ldp-mpls', REFERENCE_CLASS, 'LdpMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.LdpMpls', 
                [], [], 
                '''                Collection for labels distribution protocol
                ''',
                'ldp_mpls',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('memory-node', REFERENCE_CLASS, 'MemoryNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.MemoryNode', 
                [], [], 
                '''                Collection for memory
                ''',
                'memory_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv2-protocol', REFERENCE_CLASS, 'Ospfv2Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.Ospfv2Protocol', 
                [], [], 
                '''                Data collection for OSPF v2 Protocol
                ''',
                'ospfv2_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv3-protocol', REFERENCE_CLASS, 'Ospfv3Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.Ospfv3Protocol', 
                [], [], 
                '''                Data collection for OSPF v3 Protocol
                ''',
                'ospfv3_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('process-node', REFERENCE_CLASS, 'ProcessNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics.ProcessNode', 
                [], [], 
                '''                Collection for process
                ''',
                'process_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the LDP Session
                ''',
                'session',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session', 
                [], [], 
                '''                IP address of the LDP Session
                ''',
                'session',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.LdpMpls' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.LdpMpls',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions', 
                [], [], 
                '''                LDP session specification
                ''',
                'sessions',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ldp-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF Instance Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospf-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances',
            False, 
            [
            _MetaInfoClassMember('ospf-instance', REFERENCE_LIST, 'OspfInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance', 
                [], [], 
                '''                Instance being monitored
                ''',
                'ospf_instance',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospf-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol',
            False, 
            [
            _MetaInfoClassMember('ospf-instances', REFERENCE_CLASS, 'OspfInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances', 
                [], [], 
                '''                Monitor an instance
                ''',
                'ospf_instances',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv3-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface', 
                [], [], 
                '''                Interface being Monitored
                ''',
                'interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.GenericCounters' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.GenericCounters',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces', 
                [], [], 
                '''                Monitor an Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'generic-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid',
            False, 
            [
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specify Process ID
                ''',
                'pid',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'pid',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids',
            False, 
            [
            _MetaInfoClassMember('pid', REFERENCE_LIST, 'Pid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid', 
                [], [], 
                '''                Specify an existing template for data
                collection
                ''',
                'pid',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'pids',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('pids', REFERENCE_CLASS, 'Pids' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids', 
                [], [], 
                '''                Process ID specification
                ''',
                'pids',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes',
            False, 
            [
            _MetaInfoClassMember('process-node', REFERENCE_LIST, 'ProcessNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode', 
                [], [], 
                '''                Node instance
                ''',
                'process_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Process' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Process',
            False, 
            [
            _MetaInfoClassMember('process-nodes', REFERENCE_CLASS, 'ProcessNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes', 
                [], [], 
                '''                Node specification
                ''',
                'process_nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface', 
                [], [], 
                '''                Interface being Monitored
                ''',
                'interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.BasicCounters' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.BasicCounters',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces', 
                [], [], 
                '''                Monitor an Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'basic-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Memory.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Memory.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node', 
                [], [], 
                '''                Node instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Memory' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Memory',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Memory.Nodes', 
                [], [], 
                '''                Node specification
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'memory',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF Instance Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospf-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances',
            False, 
            [
            _MetaInfoClassMember('ospf-instance', REFERENCE_LIST, 'OspfInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance', 
                [], [], 
                '''                Instance being monitored
                ''',
                'ospf_instance',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospf-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol',
            False, 
            [
            _MetaInfoClassMember('ospf-instances', REFERENCE_CLASS, 'OspfInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances', 
                [], [], 
                '''                Monitor an instance
                ''',
                'ospf_instances',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv2-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Cpu.Nodes' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Cpu.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node', 
                [], [], 
                '''                Node instance
                ''',
                'node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Cpu' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Cpu',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Cpu.Nodes', 
                [], [], 
                '''                Node specification
                ''',
                'nodes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'cpu',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the Neighbor
                ''',
                'peer_address',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor', 
                [], [], 
                '''                Neighbor being monitored
                ''',
                'neighbor',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.Bgp' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.Bgp',
            False, 
            [
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors', 
                [], [], 
                '''                Monitor BGP protocol for a BGP peer
                ''',
                'neighbors',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Template name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface', 
                [], [], 
                '''                Interface being Monitored
                ''',
                'interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable.DataRates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable.DataRates',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces', 
                [], [], 
                '''                Monitor an Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'data-rates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable.MonitorEnable' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable.MonitorEnable',
            False, 
            [
            _MetaInfoClassMember('basic-counters', REFERENCE_CLASS, 'BasicCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.BasicCounters', 
                [], [], 
                '''                Monitoring for basic-counters
                ''',
                'basic_counters',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Bgp', 
                [], [], 
                '''                Monitor BGP protocol
                ''',
                'bgp',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('cpu', REFERENCE_CLASS, 'Cpu' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Cpu', 
                [], [], 
                '''                Collection for CPU
                ''',
                'cpu',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('data-rates', REFERENCE_CLASS, 'DataRates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.DataRates', 
                [], [], 
                '''                Monitoring for data-rates
                ''',
                'data_rates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('generic-counters', REFERENCE_CLASS, 'GenericCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.GenericCounters', 
                [], [], 
                '''                Monitoring for generic-counters
                ''',
                'generic_counters',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ldp-mpls', REFERENCE_CLASS, 'LdpMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.LdpMpls', 
                [], [], 
                '''                Monitoring for LDP
                ''',
                'ldp_mpls',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('memory', REFERENCE_CLASS, 'Memory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Memory', 
                [], [], 
                '''                Collection for memory
                ''',
                'memory',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv2-protocol', REFERENCE_CLASS, 'Ospfv2Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol', 
                [], [], 
                '''                Monitor OSPF v2 Protocol
                ''',
                'ospfv2_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv3-protocol', REFERENCE_CLASS, 'Ospfv3Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol', 
                [], [], 
                '''                Monitor OSPF v3 Protocol
                ''',
                'ospfv3_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('process', REFERENCE_CLASS, 'Process' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable.Process', 
                [], [], 
                '''                Collection for a single process
                ''',
                'process',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'monitor-enable',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Enable' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Enable',
            False, 
            [
            _MetaInfoClassMember('monitor-enable', REFERENCE_CLASS, 'MonitorEnable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.MonitorEnable', 
                [], [], 
                '''                Start data collection for a monitored instance
                ''',
                'monitor_enable',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Statistics', 
                [], [], 
                '''                Start periodic collection using a defined a
                template
                ''',
                'statistics',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable.Threshold', 
                [], [], 
                '''                Start threshold monitoring using a defined
                template
                ''',
                'threshold',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'enable',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp',
            False, 
            [
            _MetaInfoClassMember('reg-exp-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Regular expression index number
                ''',
                'reg_exp_index',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('reg-exp-string', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                Regular expression string to match
                ''',
                'reg_exp_string',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'reg-exp',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.RegExpGroups.RegExpGroup.RegExps' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.RegExpGroups.RegExpGroup.RegExps',
            False, 
            [
            _MetaInfoClassMember('reg-exp', REFERENCE_LIST, 'RegExp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp', 
                [], [], 
                '''                Specify regular expression index number
                ''',
                'reg_exp',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'reg-exps',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.RegExpGroups.RegExpGroup' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.RegExpGroups.RegExpGroup',
            False, 
            [
            _MetaInfoClassMember('reg-exp-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Regular expression group name
                ''',
                'reg_exp_group_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('reg-exps', REFERENCE_CLASS, 'RegExps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.RegExpGroups.RegExpGroup.RegExps', 
                [], [], 
                '''                Configure regular expression
                ''',
                'reg_exps',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'reg-exp-group',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.RegExpGroups' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.RegExpGroups',
            False, 
            [
            _MetaInfoClassMember('reg-exp-group', REFERENCE_LIST, 'RegExpGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.RegExpGroups.RegExpGroup', 
                [], [], 
                '''                Specify regular expression group name
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'reg-exp-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'in-octets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'in-ucast-pkts',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'out-ucast-pkts',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'out-broadcast-pkts',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'out-multicast-pkts',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-overrun',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'out-octets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-underrun',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-total-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-total-drops',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-crc',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'in-broadcast-pkts',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'in-multicast-pkts',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'out-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-total-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'in-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-unknown-proto',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-queue-drops',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-total-drops',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-frame',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('in-broadcast-pkts', REFERENCE_CLASS, 'InBroadcastPkts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts', 
                [], [], 
                '''                Number of inbound broadcast packets
                ''',
                'in_broadcast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('in-multicast-pkts', REFERENCE_CLASS, 'InMulticastPkts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts', 
                [], [], 
                '''                Number of inbound multicast packets
                ''',
                'in_multicast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('in-octets', REFERENCE_CLASS, 'InOctets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets', 
                [], [], 
                '''                Number of inbound octets/bytes
                ''',
                'in_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('in-packets', REFERENCE_CLASS, 'InPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets', 
                [], [], 
                '''                Number of inbound packets
                ''',
                'in_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('in-ucast-pkts', REFERENCE_CLASS, 'InUcastPkts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts', 
                [], [], 
                '''                Number of inbound unicast packets
                ''',
                'in_ucast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-crc', REFERENCE_CLASS, 'InputCrc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc', 
                [], [], 
                '''                Number of inbound packets discarded with
                incorrect CRC
                ''',
                'input_crc',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-frame', REFERENCE_CLASS, 'InputFrame' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame', 
                [], [], 
                '''                Number of inbound packets with framing
                errors
                ''',
                'input_frame',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-overrun', REFERENCE_CLASS, 'InputOverrun' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun', 
                [], [], 
                '''                Number of inbound packets with overrun
                errors
                ''',
                'input_overrun',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-queue-drops', REFERENCE_CLASS, 'InputQueueDrops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops', 
                [], [], 
                '''                Number of input queue drops
                ''',
                'input_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-total-drops', REFERENCE_CLASS, 'InputTotalDrops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops', 
                [], [], 
                '''                Number of inbound correct packets discarded
                ''',
                'input_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-total-errors', REFERENCE_CLASS, 'InputTotalErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors', 
                [], [], 
                '''                Number of inbound incorrect packets
                discarded
                ''',
                'input_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-unknown-proto', REFERENCE_CLASS, 'InputUnknownProto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto', 
                [], [], 
                '''                Number of inbound packets discarded with
                unknown protocol
                ''',
                'input_unknown_proto',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('out-broadcast-pkts', REFERENCE_CLASS, 'OutBroadcastPkts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts', 
                [], [], 
                '''                Number of outbound broadcast packets
                ''',
                'out_broadcast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('out-multicast-pkts', REFERENCE_CLASS, 'OutMulticastPkts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts', 
                [], [], 
                '''                Number of outbound multicast packets
                ''',
                'out_multicast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('out-octets', REFERENCE_CLASS, 'OutOctets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets', 
                [], [], 
                '''                Number of outbound octets/bytes
                ''',
                'out_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('out-packets', REFERENCE_CLASS, 'OutPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets', 
                [], [], 
                '''                Number of outbound packets
                ''',
                'out_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('out-ucast-pkts', REFERENCE_CLASS, 'OutUcastPkts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts', 
                [], [], 
                '''                Number of outbound unicast packets
                ''',
                'out_ucast_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-total-drops', REFERENCE_CLASS, 'OutputTotalDrops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops', 
                [], [], 
                '''                Number of outbound correct packets discarded
                ''',
                'output_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-total-errors', REFERENCE_CLASS, 'OutputTotalErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors', 
                [], [], 
                '''                Number of outbound incorrect packets
                discarded
                ''',
                'output_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-underrun', REFERENCE_CLASS, 'OutputUnderrun' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun', 
                [], [], 
                '''                Number of outbound packets with underrun
                errors
                ''',
                'output_underrun',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by VRF name regular
                expression 
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'generic-counter-interface-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates',
            False, 
            [
            _MetaInfoClassMember('generic-counter-interface-template', REFERENCE_LIST, 'GenericCounterInterfaceTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate', 
                [], [], 
                '''                Interface Generic Counter threshold template
                instance
                ''',
                'generic_counter_interface_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'generic-counter-interface-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.GenericCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.GenericCounterInterface',
            False, 
            [
            _MetaInfoClassMember('generic-counter-interface-templates', REFERENCE_CLASS, 'GenericCounterInterfaceTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates', 
                [], [], 
                '''                Interface Generic Counter threshold templates
                ''',
                'generic_counter_interface_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'generic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'address-withdraw-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'label-withdraw-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'address-withdraw-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'label-withdraw-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'notification-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65536')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'total-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'notification-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'total-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'label-release-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'init-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'label-release-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'init-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'label-mapping-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'keepalive-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'label-mapping-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'keepalive-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'address-msgs-rcvd',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'address-msgs-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('address-msgs-rcvd', REFERENCE_CLASS, 'AddressMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd', 
                [], [], 
                '''                Number of Address messages received
                ''',
                'address_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('address-msgs-sent', REFERENCE_CLASS, 'AddressMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent', 
                [], [], 
                '''                Number of Address messages sent
                ''',
                'address_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('address-withdraw-msgs-rcvd', REFERENCE_CLASS, 'AddressWithdrawMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd', 
                [], [], 
                '''                Number of Address Withdraw messages received
                ''',
                'address_withdraw_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('address-withdraw-msgs-sent', REFERENCE_CLASS, 'AddressWithdrawMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent', 
                [], [], 
                '''                Number of Address Withdraw messages sent
                ''',
                'address_withdraw_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('init-msgs-rcvd', REFERENCE_CLASS, 'InitMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd', 
                [], [], 
                '''                Number of Init messages received
                ''',
                'init_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('init-msgs-sent', REFERENCE_CLASS, 'InitMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent', 
                [], [], 
                '''                Number of Init messages sent
                ''',
                'init_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('keepalive-msgs-rcvd', REFERENCE_CLASS, 'KeepaliveMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd', 
                [], [], 
                '''                Number of Keepalive messages received
                ''',
                'keepalive_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('keepalive-msgs-sent', REFERENCE_CLASS, 'KeepaliveMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent', 
                [], [], 
                '''                Number of Keepalive messages sent
                ''',
                'keepalive_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('label-mapping-msgs-rcvd', REFERENCE_CLASS, 'LabelMappingMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd', 
                [], [], 
                '''                Number of Label Mapping messages received
                ''',
                'label_mapping_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('label-mapping-msgs-sent', REFERENCE_CLASS, 'LabelMappingMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent', 
                [], [], 
                '''                Number of Label Mapping messages sent
                ''',
                'label_mapping_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('label-release-msgs-rcvd', REFERENCE_CLASS, 'LabelReleaseMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd', 
                [], [], 
                '''                Number of LAbel Release messages received
                ''',
                'label_release_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('label-release-msgs-sent', REFERENCE_CLASS, 'LabelReleaseMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent', 
                [], [], 
                '''                Number of Label Release messages sent
                ''',
                'label_release_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('label-withdraw-msgs-rcvd', REFERENCE_CLASS, 'LabelWithdrawMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd', 
                [], [], 
                '''                Number of Label Withdraw messages received
                ''',
                'label_withdraw_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('label-withdraw-msgs-sent', REFERENCE_CLASS, 'LabelWithdrawMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent', 
                [], [], 
                '''                Number of Label Withdraw messages sent
                ''',
                'label_withdraw_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('notification-msgs-rcvd', REFERENCE_CLASS, 'NotificationMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd', 
                [], [], 
                '''                Number of Notification messages received
                ''',
                'notification_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('notification-msgs-sent', REFERENCE_CLASS, 'NotificationMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent', 
                [], [], 
                '''                Number of Notification messages sent
                ''',
                'notification_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('total-msgs-rcvd', REFERENCE_CLASS, 'TotalMsgsRcvd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd', 
                [], [], 
                '''                Total number of messages received
                ''',
                'total_msgs_rcvd',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('total-msgs-sent', REFERENCE_CLASS, 'TotalMsgsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent', 
                [], [], 
                '''                Total number of messages sent
                ''',
                'total_msgs_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ldp-mpls-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates',
            False, 
            [
            _MetaInfoClassMember('ldp-mpls-template', REFERENCE_LIST, 'LdpMplsTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate', 
                [], [], 
                '''                MPLS LDP threshold template instance
                ''',
                'ldp_mpls_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ldp-mpls-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.LdpMpls' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.LdpMpls',
            False, 
            [
            _MetaInfoClassMember('ldp-mpls-templates', REFERENCE_CLASS, 'LdpMplsTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates', 
                [], [], 
                '''                MPLS LDP threshold templates
                ''',
                'ldp_mpls_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ldp-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'in-octets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'out-octets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-queue-drops',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-total-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-total-drops',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'out-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-total-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'in-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-queue-drops',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-total-drops',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('in-octets', REFERENCE_CLASS, 'InOctets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets', 
                [], [], 
                '''                Number of inbound octets/bytes
                ''',
                'in_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('in-packets', REFERENCE_CLASS, 'InPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets', 
                [], [], 
                '''                Number of inbound packets
                ''',
                'in_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-queue-drops', REFERENCE_CLASS, 'InputQueueDrops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops', 
                [], [], 
                '''                Number of input queue drops
                ''',
                'input_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-total-drops', REFERENCE_CLASS, 'InputTotalDrops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops', 
                [], [], 
                '''                Number of inbound correct packets discarded
                ''',
                'input_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-total-errors', REFERENCE_CLASS, 'InputTotalErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors', 
                [], [], 
                '''                Number of inbound incorrect packets
                discarded
                ''',
                'input_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('out-octets', REFERENCE_CLASS, 'OutOctets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets', 
                [], [], 
                '''                Number of outbound octets/bytes
                ''',
                'out_octets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('out-packets', REFERENCE_CLASS, 'OutPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets', 
                [], [], 
                '''                Number of outbound packets
                ''',
                'out_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-queue-drops', REFERENCE_CLASS, 'OutputQueueDrops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops', 
                [], [], 
                '''                Number of outbound queue drops
                ''',
                'output_queue_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-total-drops', REFERENCE_CLASS, 'OutputTotalDrops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops', 
                [], [], 
                '''                Number of outbound correct packets discarded
                ''',
                'output_total_drops',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-total-errors', REFERENCE_CLASS, 'OutputTotalErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors', 
                [], [], 
                '''                Number of outbound incorrect packets
                discarded
                ''',
                'output_total_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by VRF name regular
                expression 
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'basic-counter-interface-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interface-template', REFERENCE_LIST, 'BasicCounterInterfaceTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate', 
                [], [], 
                '''                Interface Basic Counter threshold template
                instance
                ''',
                'basic_counter_interface_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'basic-counter-interface-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.BasicCounterInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.BasicCounterInterface',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interface-templates', REFERENCE_CLASS, 'BasicCounterInterfaceTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates', 
                [], [], 
                '''                Interface Basic Counter threshold templates
                ''',
                'basic_counter_interface_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'basic-counter-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-update-messages',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'errors-received',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'conn-established',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-messages',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'conn-dropped',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-update-messages',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'errors-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-messages',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('conn-dropped', REFERENCE_CLASS, 'ConnDropped' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped', 
                [], [], 
                '''                Number of times the connection was dropped
                ''',
                'conn_dropped',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('conn-established', REFERENCE_CLASS, 'ConnEstablished' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished', 
                [], [], 
                '''                Number of times the connection was
                established
                ''',
                'conn_established',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('errors-received', REFERENCE_CLASS, 'ErrorsReceived' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived', 
                [], [], 
                '''                Number of error notifications received
                ''',
                'errors_received',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('errors-sent', REFERENCE_CLASS, 'ErrorsSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent', 
                [], [], 
                '''                Number of error notifications sent
                ''',
                'errors_sent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-messages', REFERENCE_CLASS, 'InputMessages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages', 
                [], [], 
                '''                Number of messages received
                ''',
                'input_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-update-messages', REFERENCE_CLASS, 'InputUpdateMessages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages', 
                [], [], 
                '''                Number of update messages received
                ''',
                'input_update_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-messages', REFERENCE_CLASS, 'OutputMessages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages', 
                [], [], 
                '''                Number of messages sent
                ''',
                'output_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-update-messages', REFERENCE_CLASS, 'OutputUpdateMessages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages', 
                [], [], 
                '''                Number of update messages sent
                ''',
                'output_update_messages',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'bgp-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp.BgpTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp.BgpTemplates',
            False, 
            [
            _MetaInfoClassMember('bgp-template', REFERENCE_LIST, 'BgpTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate', 
                [], [], 
                '''                BGP threshold template instance
                ''',
                'bgp_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'bgp-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Bgp' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Bgp',
            False, 
            [
            _MetaInfoClassMember('bgp-templates', REFERENCE_CLASS, 'BgpTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp.BgpTemplates', 
                [], [], 
                '''                BGP threshold templates
                ''',
                'bgp_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'checksum-errors',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-lsa-acks-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-db-ds-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-db-ds-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-lsa-updates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-db-ds',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-lsa-updates-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-db-ds',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-lsa-updates-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-hello-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-hello-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-ls-requests',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-lsa-acks-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-lsa-acks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-lsa-acks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-lsa-updates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-ls-requests-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-ls-requests-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-ls-requests',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('checksum-errors', REFERENCE_CLASS, 'ChecksumErrors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors', 
                [], [], 
                '''                Number of packets received with checksum
                errors
                ''',
                'checksum_errors',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-db-ds', REFERENCE_CLASS, 'InputDbDs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs', 
                [], [], 
                '''                Number of DBD packets received
                ''',
                'input_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-db-ds-lsa', REFERENCE_CLASS, 'InputDbDsLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa', 
                [], [], 
                '''                Number of LSA received in DBD packets
                ''',
                'input_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-hello-packets', REFERENCE_CLASS, 'InputHelloPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets', 
                [], [], 
                '''                Number of Hello packets received
                ''',
                'input_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-ls-requests', REFERENCE_CLASS, 'InputLsRequests' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests', 
                [], [], 
                '''                Number of LS Requests received
                ''',
                'input_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-ls-requests-lsa', REFERENCE_CLASS, 'InputLsRequestsLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa', 
                [], [], 
                '''                Number of LSA received in LS Requests
                ''',
                'input_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-lsa-acks', REFERENCE_CLASS, 'InputLsaAcks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks', 
                [], [], 
                '''                Number of LSA Acknowledgements received
                ''',
                'input_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-lsa-acks-lsa', REFERENCE_CLASS, 'InputLsaAcksLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa', 
                [], [], 
                '''                Number of LSA received in LSA Acknowledgements
                ''',
                'input_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-lsa-updates', REFERENCE_CLASS, 'InputLsaUpdates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates', 
                [], [], 
                '''                Number of LSA Updates received
                ''',
                'input_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-lsa-updates-lsa', REFERENCE_CLASS, 'InputLsaUpdatesLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa', 
                [], [], 
                '''                Number of LSA received in LSA Updates
                ''',
                'input_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-packets', REFERENCE_CLASS, 'InputPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets', 
                [], [], 
                '''                Total number of packets received
                ''',
                'input_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-db-ds', REFERENCE_CLASS, 'OutputDbDs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs', 
                [], [], 
                '''                Number of DBD packets sent
                ''',
                'output_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-db-ds-lsa', REFERENCE_CLASS, 'OutputDbDsLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa', 
                [], [], 
                '''                Number of LSA sent in DBD packets
                ''',
                'output_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-hello-packets', REFERENCE_CLASS, 'OutputHelloPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets', 
                [], [], 
                '''                Total number of packets sent
                ''',
                'output_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-ls-requests', REFERENCE_CLASS, 'OutputLsRequests' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests', 
                [], [], 
                '''                Number of LS Requests sent
                ''',
                'output_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-ls-requests-lsa', REFERENCE_CLASS, 'OutputLsRequestsLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa', 
                [], [], 
                '''                Number of LSA sent in LS Requests
                ''',
                'output_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-lsa-acks', REFERENCE_CLASS, 'OutputLsaAcks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks', 
                [], [], 
                '''                Number of LSA Acknowledgements sent
                ''',
                'output_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-lsa-acks-lsa', REFERENCE_CLASS, 'OutputLsaAcksLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa', 
                [], [], 
                '''                Number of LSA sent in LSA Acknowledgements
                ''',
                'output_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-lsa-updates', REFERENCE_CLASS, 'OutputLsaUpdates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates', 
                [], [], 
                '''                Number of LSA Updates sent
                ''',
                'output_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-lsa-updates-lsa', REFERENCE_CLASS, 'OutputLsaUpdatesLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa', 
                [], [], 
                '''                Number of LSA sent in LSA Updates
                ''',
                'output_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-packets', REFERENCE_CLASS, 'OutputPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets', 
                [], [], 
                '''                Total number of packets sent
                ''',
                'output_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv2-protocol-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates',
            False, 
            [
            _MetaInfoClassMember('ospfv2-protocol-template', REFERENCE_LIST, 'Ospfv2ProtocolTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate', 
                [], [], 
                '''                OSPF v2 Protocol threshold template instance
                ''',
                'ospfv2_protocol_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv2-protocol-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv2Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv2Protocol',
            False, 
            [
            _MetaInfoClassMember('ospfv2-protocol-templates', REFERENCE_CLASS, 'Ospfv2ProtocolTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates', 
                [], [], 
                '''                OSPF v2 Protocol threshold templates
                ''',
                'ospfv2_protocol_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv2-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'average-cpu-used',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'no-processes',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('average-cpu-used', REFERENCE_CLASS, 'AverageCpuUsed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed', 
                [], [], 
                '''                Average %CPU utilization
                ''',
                'average_cpu_used',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('no-processes', REFERENCE_CLASS, 'NoProcesses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses', 
                [], [], 
                '''                Number of processes
                ''',
                'no_processes',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'cpu-node-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.CpuNode.CpuNodeTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.CpuNode.CpuNodeTemplates',
            False, 
            [
            _MetaInfoClassMember('cpu-node-template', REFERENCE_LIST, 'CpuNodeTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate', 
                [], [], 
                '''                Node CPU threshold configuration template
                instances
                ''',
                'cpu_node_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'cpu-node-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.CpuNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.CpuNode',
            False, 
            [
            _MetaInfoClassMember('cpu-node-templates', REFERENCE_CLASS, 'CpuNodeTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.CpuNode.CpuNodeTemplates', 
                [], [], 
                '''                Node CPU threshold configuration templates
                ''',
                'cpu_node_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'cpu-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-data-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-packet-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-peak-pkts',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-data-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-packet-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-peak-pkts',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth', 
                [], [], 
                '''                Bandwidth in kbps
                ''',
                'bandwidth',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-data-rate', REFERENCE_CLASS, 'InputDataRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate', 
                [], [], 
                '''                Input data rate in kbps
                ''',
                'input_data_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-packet-rate', REFERENCE_CLASS, 'InputPacketRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate', 
                [], [], 
                '''                Number of input packets per second
                ''',
                'input_packet_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-peak-pkts', REFERENCE_CLASS, 'InputPeakPkts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts', 
                [], [], 
                '''                Maximum number of input packets per second
                ''',
                'input_peak_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-peak-rate', REFERENCE_CLASS, 'InputPeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate', 
                [], [], 
                '''                Peak input data rate in kbps
                ''',
                'input_peak_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-data-rate', REFERENCE_CLASS, 'OutputDataRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate', 
                [], [], 
                '''                Output data rate in kbps
                ''',
                'output_data_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-packet-rate', REFERENCE_CLASS, 'OutputPacketRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate', 
                [], [], 
                '''                Number of Output packets per second
                ''',
                'output_packet_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-peak-pkts', REFERENCE_CLASS, 'OutputPeakPkts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts', 
                [], [], 
                '''                Maximum number of output packets per second
                ''',
                'output_peak_pkts',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-peak-rate', REFERENCE_CLASS, 'OutputPeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate', 
                [], [], 
                '''                Peak output data rate in kbps
                ''',
                'output_peak_rate',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by regular expression
                ''',
                'reg_exp_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('vrf-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enable instance filtering by VRF name regular
                expression 
                ''',
                'vrf_group',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'data-rate-interface-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates',
            False, 
            [
            _MetaInfoClassMember('data-rate-interface-template', REFERENCE_LIST, 'DataRateInterfaceTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate', 
                [], [], 
                '''                Interface Data Rates threshold template
                instance
                ''',
                'data_rate_interface_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'data-rate-interface-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.DataRateInterface' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.DataRateInterface',
            False, 
            [
            _MetaInfoClassMember('data-rate-interface-templates', REFERENCE_CLASS, 'DataRateInterfaceTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates', 
                [], [], 
                '''                Interface Data Rates threshold templates
                ''',
                'data_rate_interface_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'data-rate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'average-cpu-used',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'peak-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '32767')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '32767')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'no-threads',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('average-cpu-used', REFERENCE_CLASS, 'AverageCpuUsed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed', 
                [], [], 
                '''                Average %CPU utilization
                ''',
                'average_cpu_used',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('no-threads', REFERENCE_CLASS, 'NoThreads' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads', 
                [], [], 
                '''                Number of threads
                ''',
                'no_threads',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('peak-memory', REFERENCE_CLASS, 'PeakMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory', 
                [], [], 
                '''                Max memory (KBytes) used since startup time
                ''',
                'peak_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process-node-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates',
            False, 
            [
            _MetaInfoClassMember('process-node-template', REFERENCE_LIST, 'ProcessNodeTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate', 
                [], [], 
                '''                Node Memory threshold template instance
                ''',
                'process_node_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process-node-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.ProcessNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.ProcessNode',
            False, 
            [
            _MetaInfoClassMember('process-node-templates', REFERENCE_CLASS, 'ProcessNodeTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates', 
                [], [], 
                '''                Node Memory threshold templates
                ''',
                'process_node_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'process-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4194304')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4194304')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'peak-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold end range value (for operator RG,
                set to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values
                are in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm
                type Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'curr-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('curr-memory', REFERENCE_CLASS, 'CurrMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory', 
                [], [], 
                '''                Current memory (Bytes) in use
                ''',
                'curr_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('peak-memory', REFERENCE_CLASS, 'PeakMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory', 
                [], [], 
                '''                Maximum memory (KBytes) used
                ''',
                'peak_memory',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'memory-node-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates',
            False, 
            [
            _MetaInfoClassMember('memory-node-template', REFERENCE_LIST, 'MemoryNodeTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate', 
                [], [], 
                '''                Node Memory threshold configuration template
                instance
                ''',
                'memory_node_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'memory-node-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.MemoryNode' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.MemoryNode',
            False, 
            [
            _MetaInfoClassMember('memory-node-templates', REFERENCE_CLASS, 'MemoryNodeTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates', 
                [], [], 
                '''                Node Memory threshold configuration templates
                ''',
                'memory_node_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'memory-node',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-lsa-acks-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-db-ds-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-db-ds-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-lsa-updates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-db-ds',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-lsa-updates-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-db-ds',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-lsa-updates-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-hello-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-hello-packets',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-ls-requests',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-lsa-acks-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-lsa-acks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-lsa-acks',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-lsa-updates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'output-ls-requests-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-ls-requests-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests',
            False, 
            [
            _MetaInfoClassMember('end-range-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold end range value (for operator RG, set
                to 0 otherwise)
                ''',
                'end_range_value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'PmThresholdOpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOpEnum', 
                [], [], 
                '''                Operator
                ''',
                'operator',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE if Specified threshold values are
                in percent
                ''',
                'percent',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-type', REFERENCE_ENUM_CLASS, 'PmThresholdRearmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearmEnum', 
                [], [], 
                '''                Configure the Rearm type
                ''',
                'rearm_type',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('rearm-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Configure the rearm window size (for rearm type
                Window)
                ''',
                'rearm_window',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold value (or start range value for
                operator RG)
                ''',
                'value',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'input-ls-requests',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Template Name
                ''',
                'template_name',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', True),
            _MetaInfoClassMember('input-db-ds', REFERENCE_CLASS, 'InputDbDs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs', 
                [], [], 
                '''                Number of DBD packets received
                ''',
                'input_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-db-ds-lsa', REFERENCE_CLASS, 'InputDbDsLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa', 
                [], [], 
                '''                Number of LSA received in DBD packets
                ''',
                'input_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-hello-packets', REFERENCE_CLASS, 'InputHelloPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets', 
                [], [], 
                '''                Number of Hello packets received
                ''',
                'input_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-ls-requests', REFERENCE_CLASS, 'InputLsRequests' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests', 
                [], [], 
                '''                Number of LS Requests received
                ''',
                'input_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-ls-requests-lsa', REFERENCE_CLASS, 'InputLsRequestsLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa', 
                [], [], 
                '''                Number of LSA received in LS Requests
                ''',
                'input_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-lsa-acks', REFERENCE_CLASS, 'InputLsaAcks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks', 
                [], [], 
                '''                Number of LSA Acknowledgements received
                ''',
                'input_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-lsa-acks-lsa', REFERENCE_CLASS, 'InputLsaAcksLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa', 
                [], [], 
                '''                Number of LSA received in LSA Acknowledgements
                ''',
                'input_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-lsa-updates', REFERENCE_CLASS, 'InputLsaUpdates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates', 
                [], [], 
                '''                Number of LSA Updates received
                ''',
                'input_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-lsa-updates-lsa', REFERENCE_CLASS, 'InputLsaUpdatesLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa', 
                [], [], 
                '''                Number of LSA received in LSA Updates
                ''',
                'input_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('input-packets', REFERENCE_CLASS, 'InputPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets', 
                [], [], 
                '''                Total number of packets received
                ''',
                'input_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-db-ds', REFERENCE_CLASS, 'OutputDbDs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs', 
                [], [], 
                '''                Number of DBD packets sent
                ''',
                'output_db_ds',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-db-ds-lsa', REFERENCE_CLASS, 'OutputDbDsLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa', 
                [], [], 
                '''                Number of LSA sent in DBD packets
                ''',
                'output_db_ds_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-hello-packets', REFERENCE_CLASS, 'OutputHelloPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets', 
                [], [], 
                '''                Total number of packets sent
                ''',
                'output_hello_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-ls-requests', REFERENCE_CLASS, 'OutputLsRequests' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests', 
                [], [], 
                '''                Number of LS Requests sent
                ''',
                'output_ls_requests',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-ls-requests-lsa', REFERENCE_CLASS, 'OutputLsRequestsLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa', 
                [], [], 
                '''                Number of LSA sent in LS Requests
                ''',
                'output_ls_requests_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-lsa-acks', REFERENCE_CLASS, 'OutputLsaAcks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks', 
                [], [], 
                '''                Number of LSA Acknowledgements sent
                ''',
                'output_lsa_acks',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-lsa-acks-lsa', REFERENCE_CLASS, 'OutputLsaAcksLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa', 
                [], [], 
                '''                Number of LSA sent in LSA Acknowledgements
                ''',
                'output_lsa_acks_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-lsa-updates', REFERENCE_CLASS, 'OutputLsaUpdates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates', 
                [], [], 
                '''                Number of LSA Updates sent
                ''',
                'output_lsa_updates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-lsa-updates-lsa', REFERENCE_CLASS, 'OutputLsaUpdatesLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa', 
                [], [], 
                '''                Number of LSA sent in LSA Updates
                ''',
                'output_lsa_updates_lsa',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('output-packets', REFERENCE_CLASS, 'OutputPackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets', 
                [], [], 
                '''                Total number of packets sent
                ''',
                'output_packets',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('sample-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Frequency of sampling in minutes
                ''',
                'sample_interval',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv3-protocol-template',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates',
            False, 
            [
            _MetaInfoClassMember('ospfv3-protocol-template', REFERENCE_LIST, 'Ospfv3ProtocolTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate', 
                [], [], 
                '''                OSPF v2 Protocol threshold template instance
                ''',
                'ospfv3_protocol_template',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv3-protocol-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold.Ospfv3Protocol' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold.Ospfv3Protocol',
            False, 
            [
            _MetaInfoClassMember('ospfv3-protocol-templates', REFERENCE_CLASS, 'Ospfv3ProtocolTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates', 
                [], [], 
                '''                OSPF v2 Protocol threshold templates
                ''',
                'ospfv3_protocol_templates',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'ospfv3-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt.Threshold' : {
        'meta_info' : _MetaInfoClass('PerfMgmt.Threshold',
            False, 
            [
            _MetaInfoClassMember('basic-counter-interface', REFERENCE_CLASS, 'BasicCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.BasicCounterInterface', 
                [], [], 
                '''                Interface Basic Counter threshold configuration
                ''',
                'basic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Bgp', 
                [], [], 
                '''                BGP threshold configuration
                ''',
                'bgp',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('cpu-node', REFERENCE_CLASS, 'CpuNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.CpuNode', 
                [], [], 
                '''                Node CPU threshold configuration
                ''',
                'cpu_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('data-rate-interface', REFERENCE_CLASS, 'DataRateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.DataRateInterface', 
                [], [], 
                '''                Interface Data Rates threshold configuration
                ''',
                'data_rate_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('generic-counter-interface', REFERENCE_CLASS, 'GenericCounterInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.GenericCounterInterface', 
                [], [], 
                '''                Interface Generic Counter threshold
                configuration
                ''',
                'generic_counter_interface',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ldp-mpls', REFERENCE_CLASS, 'LdpMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.LdpMpls', 
                [], [], 
                '''                MPLS LDP threshold configuration
                ''',
                'ldp_mpls',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('memory-node', REFERENCE_CLASS, 'MemoryNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.MemoryNode', 
                [], [], 
                '''                Node Memory threshold configuration
                ''',
                'memory_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv2-protocol', REFERENCE_CLASS, 'Ospfv2Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv2Protocol', 
                [], [], 
                '''                OSPF v2 Protocol threshold configuration
                ''',
                'ospfv2_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('ospfv3-protocol', REFERENCE_CLASS, 'Ospfv3Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.Ospfv3Protocol', 
                [], [], 
                '''                OSPF v2 Protocol threshold configuration
                ''',
                'ospfv3_protocol',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('process-node', REFERENCE_CLASS, 'ProcessNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold.ProcessNode', 
                [], [], 
                '''                Node Process threshold configuration
                ''',
                'process_node',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
    'PerfMgmt' : {
        'meta_info' : _MetaInfoClass('PerfMgmt',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_CLASS, 'Enable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Enable', 
                [], [], 
                '''                Start data collection and/or threshold
                monitoring
                ''',
                'enable',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('reg-exp-groups', REFERENCE_CLASS, 'RegExpGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.RegExpGroups', 
                [], [], 
                '''                Configure regular expression group
                ''',
                'reg_exp_groups',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('resources', REFERENCE_CLASS, 'Resources' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Resources', 
                [], [], 
                '''                Resources configuration
                ''',
                'resources',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Statistics', 
                [], [], 
                '''                Templates for collection of statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PerfMgmt.Threshold', 
                [], [], 
                '''                Container for threshold templates
                ''',
                'threshold',
                'Cisco-IOS-XR-manageability-perfmgmt-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-perfmgmt-cfg',
            'perf-mgmt',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-perfmgmt-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg'
        ),
    },
}
_meta_table['PerfMgmt.Resources.TftpResources']['meta_info'].parent =_meta_table['PerfMgmt.Resources']['meta_info']
_meta_table['PerfMgmt.Resources.DumpLocal']['meta_info'].parent =_meta_table['PerfMgmt.Resources']['meta_info']
_meta_table['PerfMgmt.Resources.MemoryResources']['meta_info'].parent =_meta_table['PerfMgmt.Resources']['meta_info']
_meta_table['PerfMgmt.Statistics.GenericCounterInterface.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.GenericCounterInterface.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.GenericCounterInterface.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.GenericCounterInterface']['meta_info']
_meta_table['PerfMgmt.Statistics.ProcessNode.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.ProcessNode.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.ProcessNode.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.ProcessNode']['meta_info']
_meta_table['PerfMgmt.Statistics.BasicCounterInterface.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.BasicCounterInterface.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.BasicCounterInterface.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.BasicCounterInterface']['meta_info']
_meta_table['PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.Ospfv3Protocol.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.Ospfv3Protocol.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.Ospfv3Protocol']['meta_info']
_meta_table['PerfMgmt.Statistics.CpuNode.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.CpuNode.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.CpuNode.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.CpuNode']['meta_info']
_meta_table['PerfMgmt.Statistics.DataRateInterface.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.DataRateInterface.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.DataRateInterface.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.DataRateInterface']['meta_info']
_meta_table['PerfMgmt.Statistics.MemoryNode.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.MemoryNode.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.MemoryNode.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.MemoryNode']['meta_info']
_meta_table['PerfMgmt.Statistics.LdpMpls.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.LdpMpls.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.LdpMpls.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.LdpMpls']['meta_info']
_meta_table['PerfMgmt.Statistics.Bgp.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.Bgp.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.Bgp.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.Bgp']['meta_info']
_meta_table['PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.Ospfv2Protocol.Templates']['meta_info']
_meta_table['PerfMgmt.Statistics.Ospfv2Protocol.Templates']['meta_info'].parent =_meta_table['PerfMgmt.Statistics.Ospfv2Protocol']['meta_info']
_meta_table['PerfMgmt.Statistics.GenericCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.ProcessNode']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.BasicCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.Ospfv3Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.CpuNode']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.DataRateInterface']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.MemoryNode']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.LdpMpls']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.Bgp']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Statistics.Ospfv2Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.MemoryNode.Nodes']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.MemoryNode.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.MemoryNode']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.MemoryNode.NodeAll']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.MemoryNode']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.CpuNode.Nodes']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.CpuNode.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.CpuNode']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.CpuNode.NodeAll']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.CpuNode']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.ProcessNode.Nodes']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.ProcessNode.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.ProcessNode']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.ProcessNode.NodeAll']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold.ProcessNode']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.Ospfv3Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.Bgp']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.DataRateInterface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.Ospfv2Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.MemoryNode']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.GenericCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.CpuNode']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.LdpMpls']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.ProcessNode']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold.BasicCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Threshold']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.CpuNode.Nodes']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.CpuNode.NodeAll']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.CpuNode']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.CpuNode.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.CpuNode']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.ProcessNode.Nodes']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.ProcessNode.NodeAll']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.ProcessNode']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.ProcessNode.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.ProcessNode']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.MemoryNode.Nodes']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.MemoryNode.NodeAll']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.MemoryNode']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.MemoryNode.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics.MemoryNode']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.GenericCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.Bgp']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.Ospfv2Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.Ospfv3Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.CpuNode']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.BasicCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.ProcessNode']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.DataRateInterface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.MemoryNode']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics.LdpMpls']['meta_info'].parent =_meta_table['PerfMgmt.Enable.Statistics']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.LdpMpls']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.GenericCounters']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Process']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.BasicCounters']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Memory.Nodes']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Memory.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Memory']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Cpu.Nodes']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Cpu.Nodes']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Cpu']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.Bgp']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable.DataRates']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.LdpMpls']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.GenericCounters']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Process']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.BasicCounters']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Memory']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Cpu']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.Bgp']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable.DataRates']['meta_info'].parent =_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']
_meta_table['PerfMgmt.Enable.Threshold']['meta_info'].parent =_meta_table['PerfMgmt.Enable']['meta_info']
_meta_table['PerfMgmt.Enable.Statistics']['meta_info'].parent =_meta_table['PerfMgmt.Enable']['meta_info']
_meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info'].parent =_meta_table['PerfMgmt.Enable']['meta_info']
_meta_table['PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp']['meta_info'].parent =_meta_table['PerfMgmt.RegExpGroups.RegExpGroup.RegExps']['meta_info']
_meta_table['PerfMgmt.RegExpGroups.RegExpGroup.RegExps']['meta_info'].parent =_meta_table['PerfMgmt.RegExpGroups.RegExpGroup']['meta_info']
_meta_table['PerfMgmt.RegExpGroups.RegExpGroup']['meta_info'].parent =_meta_table['PerfMgmt.RegExpGroups']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.GenericCounterInterface']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.LdpMpls']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.BasicCounterInterface']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Bgp']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv2Protocol']['meta_info']
_meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.CpuNode']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.DataRateInterface']['meta_info']
_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.ProcessNode']['meta_info']
_meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.MemoryNode']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates']['meta_info'].parent =_meta_table['PerfMgmt.Threshold.Ospfv3Protocol']['meta_info']
_meta_table['PerfMgmt.Threshold.GenericCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.LdpMpls']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.BasicCounterInterface']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.Bgp']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv2Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.CpuNode']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.DataRateInterface']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.ProcessNode']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.MemoryNode']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Threshold.Ospfv3Protocol']['meta_info'].parent =_meta_table['PerfMgmt.Threshold']['meta_info']
_meta_table['PerfMgmt.Resources']['meta_info'].parent =_meta_table['PerfMgmt']['meta_info']
_meta_table['PerfMgmt.Statistics']['meta_info'].parent =_meta_table['PerfMgmt']['meta_info']
_meta_table['PerfMgmt.Enable']['meta_info'].parent =_meta_table['PerfMgmt']['meta_info']
_meta_table['PerfMgmt.RegExpGroups']['meta_info'].parent =_meta_table['PerfMgmt']['meta_info']
_meta_table['PerfMgmt.Threshold']['meta_info'].parent =_meta_table['PerfMgmt']['meta_info']
