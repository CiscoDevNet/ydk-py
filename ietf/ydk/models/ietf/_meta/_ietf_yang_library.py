


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ModulesState.Module.Deviation' : {
        'meta_info' : _MetaInfoClass('ModulesState.Module.Deviation',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-zA-Z_][a-zA-Z0-9\\-_.]*'], 
                '''                The YANG module or submodule name.
                ''',
                'name',
                'ietf-yang-library', True),
            _MetaInfoClassMember('revision', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The YANG module or submodule revision date.
                A zero-length string is used if no revision statement
                is present in the YANG module or submodule.
                ''',
                'revision',
                'ietf-yang-library', True, [
                    _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                        [], [b'\\d{4}-\\d{2}-\\d{2}'], 
                        '''                        The YANG module or submodule revision date.
                        A zero-length string is used if no revision statement
                        is present in the YANG module or submodule.
                        ''',
                        'revision',
                        'ietf-yang-library', True),
                    _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                        [(0, None)], [], 
                        '''                        The YANG module or submodule revision date.
                        A zero-length string is used if no revision statement
                        is present in the YANG module or submodule.
                        ''',
                        'revision',
                        'ietf-yang-library', True),
                ]),
            ],
            'ietf-yang-library',
            'deviation',
            _yang_ns._namespaces['ietf-yang-library'],
        'ydk.models.ietf.ietf_yang_library'
        ),
    },
    'ModulesState.Module.Submodule' : {
        'meta_info' : _MetaInfoClass('ModulesState.Module.Submodule',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-zA-Z_][a-zA-Z0-9\\-_.]*'], 
                '''                The YANG module or submodule name.
                ''',
                'name',
                'ietf-yang-library', True),
            _MetaInfoClassMember('revision', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The YANG module or submodule revision date.
                A zero-length string is used if no revision statement
                is present in the YANG module or submodule.
                ''',
                'revision',
                'ietf-yang-library', True, [
                    _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                        [], [b'\\d{4}-\\d{2}-\\d{2}'], 
                        '''                        The YANG module or submodule revision date.
                        A zero-length string is used if no revision statement
                        is present in the YANG module or submodule.
                        ''',
                        'revision',
                        'ietf-yang-library', True),
                    _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                        [(0, None)], [], 
                        '''                        The YANG module or submodule revision date.
                        A zero-length string is used if no revision statement
                        is present in the YANG module or submodule.
                        ''',
                        'revision',
                        'ietf-yang-library', True),
                ]),
            _MetaInfoClassMember('schema', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Contains a URL that represents the YANG schema
                resource for this module or submodule.
                This leaf will only be present if there is a URL
                available for retrieval of the schema for this entry.
                ''',
                'schema',
                'ietf-yang-library', False),
            ],
            'ietf-yang-library',
            'submodule',
            _yang_ns._namespaces['ietf-yang-library'],
        'ydk.models.ietf.ietf_yang_library'
        ),
    },
    'ModulesState.Module.ConformanceTypeEnum' : _MetaInfoEnum('ConformanceTypeEnum', 'ydk.models.ietf.ietf_yang_library',
        {
            'implement':'implement',
            'import':'import_',
        }, 'ietf-yang-library', _yang_ns._namespaces['ietf-yang-library']),
    'ModulesState.Module' : {
        'meta_info' : _MetaInfoClass('ModulesState.Module',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-zA-Z_][a-zA-Z0-9\\-_.]*'], 
                '''                The YANG module or submodule name.
                ''',
                'name',
                'ietf-yang-library', True),
            _MetaInfoClassMember('revision', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The YANG module or submodule revision date.
                A zero-length string is used if no revision statement
                is present in the YANG module or submodule.
                ''',
                'revision',
                'ietf-yang-library', True, [
                    _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                        [], [b'\\d{4}-\\d{2}-\\d{2}'], 
                        '''                        The YANG module or submodule revision date.
                        A zero-length string is used if no revision statement
                        is present in the YANG module or submodule.
                        ''',
                        'revision',
                        'ietf-yang-library', True),
                    _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                        [(0, None)], [], 
                        '''                        The YANG module or submodule revision date.
                        A zero-length string is used if no revision statement
                        is present in the YANG module or submodule.
                        ''',
                        'revision',
                        'ietf-yang-library', True),
                ]),
            _MetaInfoClassMember('conformance-type', REFERENCE_ENUM_CLASS, 'ConformanceTypeEnum' , 'ydk.models.ietf.ietf_yang_library', 'ModulesState.Module.ConformanceTypeEnum', 
                [], [], 
                '''                Indicates the type of conformance the server is claiming
                for the YANG module identified by this entry.
                ''',
                'conformance_type',
                'ietf-yang-library', False),
            _MetaInfoClassMember('deviation', REFERENCE_LIST, 'Deviation' , 'ydk.models.ietf.ietf_yang_library', 'ModulesState.Module.Deviation', 
                [], [], 
                '''                List of YANG deviation module names and revisions
                used by this server to modify the conformance of
                the module associated with this entry.  Note that
                the same module can be used for deviations for
                multiple modules, so the same entry MAY appear
                within multiple 'module' entries.
                The deviation module MUST be present in the 'module'
                list, with the same name and revision values.
                The 'conformance-type' value will be 'implement' for
                the deviation module.
                ''',
                'deviation',
                'ietf-yang-library', False),
            _MetaInfoClassMember('feature', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'[a-zA-Z_][a-zA-Z0-9\\-_.]*'], 
                '''                List of YANG feature names from this module that are
                supported by the server, regardless of whether they are
                defined in the module or any included submodule.
                ''',
                'feature',
                'ietf-yang-library', False),
            _MetaInfoClassMember('namespace', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The XML namespace identifier for this module.
                ''',
                'namespace',
                'ietf-yang-library', False),
            _MetaInfoClassMember('schema', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Contains a URL that represents the YANG schema
                resource for this module or submodule.
                This leaf will only be present if there is a URL
                available for retrieval of the schema for this entry.
                ''',
                'schema',
                'ietf-yang-library', False),
            _MetaInfoClassMember('submodule', REFERENCE_LIST, 'Submodule' , 'ydk.models.ietf.ietf_yang_library', 'ModulesState.Module.Submodule', 
                [], [], 
                '''                Each entry represents one submodule within the
                parent module.
                ''',
                'submodule',
                'ietf-yang-library', False),
            ],
            'ietf-yang-library',
            'module',
            _yang_ns._namespaces['ietf-yang-library'],
        'ydk.models.ietf.ietf_yang_library'
        ),
    },
    'ModulesState' : {
        'meta_info' : _MetaInfoClass('ModulesState',
            False, 
            [
            _MetaInfoClassMember('module', REFERENCE_LIST, 'Module' , 'ydk.models.ietf.ietf_yang_library', 'ModulesState.Module', 
                [], [], 
                '''                Each entry represents one revision of one module
                currently supported by the server.
                ''',
                'module',
                'ietf-yang-library', False),
            _MetaInfoClassMember('module-set-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Contains a server-specific identifier representing
                the current set of modules and submodules.  The
                server MUST change the value of this leaf if the
                information represented by the 'module' list instances
                has changed.
                ''',
                'module_set_id',
                'ietf-yang-library', False),
            ],
            'ietf-yang-library',
            'modules-state',
            _yang_ns._namespaces['ietf-yang-library'],
        'ydk.models.ietf.ietf_yang_library'
        ),
    },
}
_meta_table['ModulesState.Module.Deviation']['meta_info'].parent =_meta_table['ModulesState.Module']['meta_info']
_meta_table['ModulesState.Module.Submodule']['meta_info'].parent =_meta_table['ModulesState.Module']['meta_info']
_meta_table['ModulesState.Module']['meta_info'].parent =_meta_table['ModulesState']['meta_info']
