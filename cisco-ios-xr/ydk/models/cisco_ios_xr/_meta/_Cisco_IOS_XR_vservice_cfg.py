


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SfcMetadataAllocEnum' : _MetaInfoEnum('SfcMetadataAllocEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg',
        {
            'type1':'type1',
        }, 'Cisco-IOS-XR-vservice-cfg', _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg']),
    'SfcMetadataType1AllocFormatEnum' : _MetaInfoEnum('SfcMetadataType1AllocFormatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg',
        {
            'dc-allocation':'dc_allocation',
        }, 'Cisco-IOS-XR-vservice-cfg', _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg']),
    'SfcMetadataDispositionActionEnum' : _MetaInfoEnum('SfcMetadataDispositionActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg',
        {
            'redirect-nexthop':'redirect_nexthop',
        }, 'Cisco-IOS-XR-vservice-cfg', _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg']),
    'SfcSfTransportEnum' : _MetaInfoEnum('SfcSfTransportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg',
        {
            'vxlan-gpe':'vxlan_gpe',
        }, 'Cisco-IOS-XR-vservice-cfg', _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg']),
    'SfcMetadataDispositionMatchEnum' : _MetaInfoEnum('SfcMetadataDispositionMatchEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg',
        {
            'type1-dcalloc-tenant-id':'type1_dcalloc_tenant_id',
        }, 'Cisco-IOS-XR-vservice-cfg', _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg']),
    'Vservice.ServiceFunctionLocator.Names.Name.Node' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionLocator.Names.Name.Node',
            False, 
            [
            _MetaInfoClassMember('ipv4-destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 destination address
                ''',
                'ipv4_destination_address',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('ipv4-source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 source address
                ''',
                'ipv4_source_address',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('transport', REFERENCE_ENUM_CLASS, 'SfcSfTransportEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'SfcSfTransportEnum', 
                [], [], 
                '''                Transport type
                ''',
                'transport',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('vni', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                VNI
                ''',
                'vni',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionLocator.Names.Name' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionLocator.Names.Name',
            False, 
            [
            _MetaInfoClassMember('function-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Service function/forwarder name
                ''',
                'function_name',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('locator-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specify locator id
                ''',
                'locator_id',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('node', REFERENCE_CLASS, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionLocator.Names.Name.Node', 
                [], [], 
                '''                configure sff/sffl
                ''',
                'node',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'name',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionLocator.Names' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionLocator.Names',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_LIST, 'Name' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionLocator.Names.Name', 
                [], [], 
                '''                service function name
                ''',
                'name',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'names',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionLocator' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionLocator',
            False, 
            [
            _MetaInfoClassMember('names', REFERENCE_CLASS, 'Names' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionLocator.Names', 
                [], [], 
                '''                Mention the sf/sff name
                ''',
                'names',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'service-function-locator',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node' : {
        'meta_info' : _MetaInfoClass('Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'SfcMetadataDispositionActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'SfcMetadataDispositionActionEnum', 
                [], [], 
                '''                action type
                ''',
                'action_type',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('match-type', REFERENCE_ENUM_CLASS, 'SfcMetadataDispositionMatchEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'SfcMetadataDispositionMatchEnum', 
                [], [], 
                '''                match type
                ''',
                'match_type',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('nexthop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 nexthop address
                ''',
                'nexthop_ipv4_address',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('tenant-id', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                24-bit tenant id
                ''',
                'tenant_id',
                'Cisco-IOS-XR-vservice-cfg', False, max_elements=4),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.MetadataDispositions.MetadataDisposition.MatchEntry' : {
        'meta_info' : _MetaInfoClass('Vservice.MetadataDispositions.MetadataDisposition.MatchEntry',
            False, 
            [
            _MetaInfoClassMember('match-entry-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                match entry name
                ''',
                'match_entry_name',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('node', REFERENCE_CLASS, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node', 
                [], [], 
                '''                configure disposition data
                ''',
                'node',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'match-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.MetadataDispositions.MetadataDisposition' : {
        'meta_info' : _MetaInfoClass('Vservice.MetadataDispositions.MetadataDisposition',
            False, 
            [
            _MetaInfoClassMember('disposition-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                disposition name
                ''',
                'disposition_name',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'SfcMetadataType1AllocFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'SfcMetadataType1AllocFormatEnum', 
                [], [], 
                '''                Specify Format
                ''',
                'format',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('match-entry', REFERENCE_LIST, 'MatchEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.MetadataDispositions.MetadataDisposition.MatchEntry', 
                [], [], 
                '''                match entry name
                ''',
                'match_entry',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'metadata-disposition',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.MetadataDispositions' : {
        'meta_info' : _MetaInfoClass('Vservice.MetadataDispositions',
            False, 
            [
            _MetaInfoClassMember('metadata-disposition', REFERENCE_LIST, 'MetadataDisposition' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.MetadataDispositions.MetadataDisposition', 
                [], [], 
                '''                metadata disposition name
                ''',
                'metadata_disposition',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'metadata-dispositions',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionForwardLocator.Names.Name.Node' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionForwardLocator.Names.Name.Node',
            False, 
            [
            _MetaInfoClassMember('ipv4-destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 destination address
                ''',
                'ipv4_destination_address',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('ipv4-source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 source address
                ''',
                'ipv4_source_address',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('transport', REFERENCE_ENUM_CLASS, 'SfcSfTransportEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'SfcSfTransportEnum', 
                [], [], 
                '''                Transport type
                ''',
                'transport',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('vni', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                VNI
                ''',
                'vni',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionForwardLocator.Names.Name' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionForwardLocator.Names.Name',
            False, 
            [
            _MetaInfoClassMember('function-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Service function/forwarder name
                ''',
                'function_name',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('locator-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specify locator id
                ''',
                'locator_id',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('node', REFERENCE_CLASS, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionForwardLocator.Names.Name.Node', 
                [], [], 
                '''                configure sff/sffl
                ''',
                'node',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'name',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionForwardLocator.Names' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionForwardLocator.Names',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_LIST, 'Name' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionForwardLocator.Names.Name', 
                [], [], 
                '''                service function name
                ''',
                'name',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'names',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionForwardLocator' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionForwardLocator',
            False, 
            [
            _MetaInfoClassMember('names', REFERENCE_CLASS, 'Names' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionForwardLocator.Names', 
                [], [], 
                '''                Mention the sf/sff name
                ''',
                'names',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'service-function-forward-locator',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.MetadataTemplates.MetadataTemplate' : {
        'meta_info' : _MetaInfoClass('Vservice.MetadataTemplates.MetadataTemplate',
            False, 
            [
            _MetaInfoClassMember('metadata-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                metadata name
                ''',
                'metadata_name',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'SfcMetadataAllocEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'SfcMetadataAllocEnum', 
                [], [], 
                '''                Specify Type 
                ''',
                'type',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'SfcMetadataType1AllocFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'SfcMetadataType1AllocFormatEnum', 
                [], [], 
                '''                Specify Format
                ''',
                'format',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('tenant-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Enter 24-bit tenant id
                ''',
                'tenant_id',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'metadata-template',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.MetadataTemplates' : {
        'meta_info' : _MetaInfoClass('Vservice.MetadataTemplates',
            False, 
            [
            _MetaInfoClassMember('metadata-template', REFERENCE_LIST, 'MetadataTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.MetadataTemplates.MetadataTemplate', 
                [], [], 
                '''                metadata name, type and format
                ''',
                'metadata_template',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'metadata-templates',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'SfcMetadataDispositionActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'SfcMetadataDispositionActionEnum', 
                [], [], 
                '''                default action enum
                ''',
                'action',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('metatdata-disposition', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                metadata-disposition name
                ''',
                'metatdata_disposition',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('nexthop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 nexthop address
                ''',
                'nexthop_ipv4_address',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                nexthop vrf name
                ''',
                'vrf',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_CLASS, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node', 
                [], [], 
                '''                configure default terminate action
                ''',
                'node',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'terminate',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Service function path
                ''',
                'enable',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('reserved', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dummy
                ''',
                'reserved',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SFF Name
                ''',
                'name',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('node', REFERENCE_CLASS, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node', 
                [], [], 
                '''                configure SFP
                ''',
                'node',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'sff-name',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames',
            False, 
            [
            _MetaInfoClassMember('sff-name', REFERENCE_LIST, 'SffName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName', 
                [], [], 
                '''                service function forwarder name
                ''',
                'sff_name',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'sff-names',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Service function path
                ''',
                'enable',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('reserved', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dummy
                ''',
                'reserved',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SF Name
                ''',
                'name',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('node', REFERENCE_CLASS, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node', 
                [], [], 
                '''                configure SFP
                ''',
                'node',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'sf-name',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames',
            False, 
            [
            _MetaInfoClassMember('sf-name', REFERENCE_LIST, 'SfName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName', 
                [], [], 
                '''                service function name
                ''',
                'sf_name',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'sf-names',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specify the id of service function
                ''',
                'index',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('sf-names', REFERENCE_CLASS, 'SfNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames', 
                [], [], 
                '''                service function 
                ''',
                'sf_names',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('sff-names', REFERENCE_CLASS, 'SffNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames', 
                [], [], 
                '''                service function forwarder 
                ''',
                'sff_names',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('terminate', REFERENCE_CLASS, 'Terminate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate', 
                [], [], 
                '''                configure terminate
                ''',
                'terminate',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'service-index',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths.Path' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Specify the service function path id
                ''',
                'path_id',
                'Cisco-IOS-XR-vservice-cfg', True),
            _MetaInfoClassMember('service-index', REFERENCE_LIST, 'ServiceIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex', 
                [], [], 
                '''                specify the service index
                ''',
                'service_index',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath.Paths' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths.Path', 
                [], [], 
                '''                specify the service function path id
                ''',
                'path',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice.ServiceFunctionPath' : {
        'meta_info' : _MetaInfoClass('Vservice.ServiceFunctionPath',
            False, 
            [
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath.Paths', 
                [], [], 
                '''                service function path id
                ''',
                'paths',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'service-function-path',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
    'Vservice' : {
        'meta_info' : _MetaInfoClass('Vservice',
            False, 
            [
            _MetaInfoClassMember('metadata-dispositions', REFERENCE_CLASS, 'MetadataDispositions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.MetadataDispositions', 
                [], [], 
                '''                Configure metadata disposition
                ''',
                'metadata_dispositions',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('metadata-templates', REFERENCE_CLASS, 'MetadataTemplates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.MetadataTemplates', 
                [], [], 
                '''                configure metadata imposition
                ''',
                'metadata_templates',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('service-function-forward-locator', REFERENCE_CLASS, 'ServiceFunctionForwardLocator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionForwardLocator', 
                [], [], 
                '''                configure service function forward locator
                ''',
                'service_function_forward_locator',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('service-function-locator', REFERENCE_CLASS, 'ServiceFunctionLocator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionLocator', 
                [], [], 
                '''                configure service function locator
                ''',
                'service_function_locator',
                'Cisco-IOS-XR-vservice-cfg', False),
            _MetaInfoClassMember('service-function-path', REFERENCE_CLASS, 'ServiceFunctionPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg', 'Vservice.ServiceFunctionPath', 
                [], [], 
                '''                service function path
                ''',
                'service_function_path',
                'Cisco-IOS-XR-vservice-cfg', False),
            ],
            'Cisco-IOS-XR-vservice-cfg',
            'vservice',
            _yang_ns._namespaces['Cisco-IOS-XR-vservice-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg'
        ),
    },
}
_meta_table['Vservice.ServiceFunctionLocator.Names.Name.Node']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionLocator.Names.Name']['meta_info']
_meta_table['Vservice.ServiceFunctionLocator.Names.Name']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionLocator.Names']['meta_info']
_meta_table['Vservice.ServiceFunctionLocator.Names']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionLocator']['meta_info']
_meta_table['Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node']['meta_info'].parent =_meta_table['Vservice.MetadataDispositions.MetadataDisposition.MatchEntry']['meta_info']
_meta_table['Vservice.MetadataDispositions.MetadataDisposition.MatchEntry']['meta_info'].parent =_meta_table['Vservice.MetadataDispositions.MetadataDisposition']['meta_info']
_meta_table['Vservice.MetadataDispositions.MetadataDisposition']['meta_info'].parent =_meta_table['Vservice.MetadataDispositions']['meta_info']
_meta_table['Vservice.ServiceFunctionForwardLocator.Names.Name.Node']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionForwardLocator.Names.Name']['meta_info']
_meta_table['Vservice.ServiceFunctionForwardLocator.Names.Name']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionForwardLocator.Names']['meta_info']
_meta_table['Vservice.ServiceFunctionForwardLocator.Names']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionForwardLocator']['meta_info']
_meta_table['Vservice.MetadataTemplates.MetadataTemplate']['meta_info'].parent =_meta_table['Vservice.MetadataTemplates']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths.Path']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths.Path']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath.Paths']['meta_info']
_meta_table['Vservice.ServiceFunctionPath.Paths']['meta_info'].parent =_meta_table['Vservice.ServiceFunctionPath']['meta_info']
_meta_table['Vservice.ServiceFunctionLocator']['meta_info'].parent =_meta_table['Vservice']['meta_info']
_meta_table['Vservice.MetadataDispositions']['meta_info'].parent =_meta_table['Vservice']['meta_info']
_meta_table['Vservice.ServiceFunctionForwardLocator']['meta_info'].parent =_meta_table['Vservice']['meta_info']
_meta_table['Vservice.MetadataTemplates']['meta_info'].parent =_meta_table['Vservice']['meta_info']
_meta_table['Vservice.ServiceFunctionPath']['meta_info'].parent =_meta_table['Vservice']['meta_info']
